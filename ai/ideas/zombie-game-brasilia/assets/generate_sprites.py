#!/usr/bin/env python3
"""
ZUMBIS DE BRASILIA — Gerador de Sprites via API
Usa OpenAI DALL-E 3 ou Stability AI para gerar sprites a partir dos art-prompts.

Pipeline:
  1. Le art-prompts.md de cada personagem/arma
  2. Gera imagens em alta resolucao (1024x1024)
  3. Downscale para tamanho final (64x64 chars, 32x32 armas) com nearest-neighbor
  4. Monta sprite sheets horizontais
  5. Exporta PNG com transparencia

Uso:
    # Via OpenAI DALL-E 3:
    export OPENAI_API_KEY="sk-..."
    python generate_sprites.py --engine dalle --personagem lula

    # Via Stability AI:
    export STABILITY_API_KEY="sk-..."
    python generate_sprites.py --engine stability --personagem lula

    # Gerar TODOS os personagens:
    python generate_sprites.py --engine dalle --all

    # Gerar so armas:
    python generate_sprites.py --engine dalle --armas

    # Dry run (mostra prompts sem gerar):
    python generate_sprites.py --dry-run --personagem lula

Formatos de saida:
    - PNG individuais: 64x64 (chars) / 32x32 (armas) com transparencia
    - Sprite sheets: horizontal strip PNG
    - Atlas JSON: formato TexturePacker para Phaser 3
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("ERRO: Pillow nao instalado. Execute: pip install Pillow")
    sys.exit(1)

BASE_DIR = Path(__file__).parent
PERSONAGENS_DIR = BASE_DIR / "personagens"
ARMAS_DIR = BASE_DIR / "armas"
OUTPUT_DIR = BASE_DIR / "generated"


def extract_prompts_from_md(md_path: Path) -> list[dict]:
    """Extrai prompts de um arquivo art-prompts.md."""
    if not md_path.exists():
        return []

    content = md_path.read_text(encoding="utf-8")
    prompts = []

    # Padroes: "### Frame Name\n```\nPrompt: ...\n```\n\n```\nNegative: ...\n```"
    # ou blocos com "Stable Diffusion / DALL-E:" seguido de ```...```
    sections = re.split(r'###\s+', content)

    for section in sections[1:]:  # Skip header
        lines = section.strip().split('\n')
        name = lines[0].strip().rstrip('#').strip()

        # Extrair blocos de codigo
        code_blocks = re.findall(r'```\n?(.*?)```', section, re.DOTALL)

        prompt = ""
        negative = ""

        for block in code_blocks:
            block = block.strip()
            if block.lower().startswith("prompt:"):
                prompt = block[len("prompt:"):].strip()
            elif block.lower().startswith("negative:"):
                negative = block[len("negative:"):].strip()
            elif "negative" not in block.lower() and len(block) > 50:
                # Bloco sem prefix — provavelmente e o prompt
                if not prompt:
                    prompt = block

        if prompt:
            prompts.append({
                "name": name,
                "prompt": prompt,
                "negative": negative,
                "source_file": str(md_path),
            })

    return prompts


def generate_dalle(prompt: str, negative: str, output_path: Path, size: str = "1024x1024"):
    """Gera imagem via OpenAI DALL-E 3."""
    try:
        from openai import OpenAI
    except ImportError:
        print("ERRO: openai nao instalado. Execute: pip install openai")
        sys.exit(1)

    client = OpenAI()

    # DALL-E 3 nao suporta negative prompts diretamente, entao incluimos no prompt
    full_prompt = prompt
    if negative:
        full_prompt += f"\n\nDo NOT include: {negative}"

    response = client.images.generate(
        model="dall-e-3",
        prompt=full_prompt[:4000],  # DALL-E 3 limit
        size=size,
        quality="standard",
        n=1,
        response_format="url",
    )

    image_url = response.data[0].url

    # Download da imagem
    import urllib.request
    urllib.request.urlretrieve(image_url, str(output_path))
    return output_path


def generate_stability(prompt: str, negative: str, output_path: Path):
    """Gera imagem via Stability AI API."""
    import requests

    api_key = os.getenv("STABILITY_API_KEY")
    if not api_key:
        print("ERRO: STABILITY_API_KEY nao definida")
        sys.exit(1)

    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={"Authorization": f"Bearer {api_key}", "Accept": "image/*"},
        files={"none": ""},
        data={
            "prompt": prompt[:10000],
            "negative_prompt": negative[:10000] if negative else "",
            "output_format": "png",
            "aspect_ratio": "1:1",
        },
    )

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    else:
        raise Exception(f"Stability API erro {response.status_code}: {response.text[:200]}")


def downscale_nearest(input_path: Path, output_path: Path, target_size: tuple[int, int]):
    """Downscale com nearest-neighbor (sem anti-alias) para pixel art."""
    img = Image.open(input_path)
    img = img.convert("RGBA")
    img = img.resize(target_size, Image.NEAREST)
    img.save(output_path, "PNG")
    return output_path


def create_sprite_sheet(frame_paths: list[Path], output_path: Path, frame_size: tuple[int, int]):
    """Monta sprite sheet horizontal a partir de frames individuais."""
    if not frame_paths:
        return

    w, h = frame_size
    sheet = Image.new("RGBA", (w * len(frame_paths), h), (0, 0, 0, 0))

    for i, path in enumerate(frame_paths):
        if path.exists():
            frame = Image.open(path).convert("RGBA").resize(frame_size, Image.NEAREST)
            sheet.paste(frame, (i * w, 0))

    sheet.save(output_path, "PNG")
    print(f"  [SHEET] {output_path.name} ({len(frame_paths)} frames, {w}x{h} each)")
    return output_path


def create_phaser_atlas_json(
    sheet_path: Path, frame_names: list[str], frame_size: tuple[int, int], output_path: Path
):
    """Gera JSON no formato TexturePacker para Phaser 3."""
    w, h = frame_size
    frames = {}
    for i, name in enumerate(frame_names):
        frames[name] = {
            "frame": {"x": i * w, "y": 0, "w": w, "h": h},
            "rotated": False,
            "trimmed": False,
            "spriteSourceSize": {"x": 0, "y": 0, "w": w, "h": h},
            "sourceSize": {"w": w, "h": h},
        }

    atlas = {
        "frames": frames,
        "meta": {
            "app": "zumbis-de-brasilia-pipeline",
            "version": "1.0",
            "image": sheet_path.name,
            "format": "RGBA8888",
            "size": {"w": w * len(frame_names), "h": h},
            "scale": "1",
        },
    }

    with open(output_path, "w") as f:
        json.dump(atlas, f, indent=2)
    print(f"  [JSON] {output_path.name} (Phaser 3 atlas)")


def process_character(name: str, engine: str, dry_run: bool = False):
    """Processa todos os sprites de um personagem."""
    char_dir = PERSONAGENS_DIR / name

    # Procurar art-prompts.md em varias locacoes possiveis
    art_prompts_path = None
    for candidate in [
        char_dir / "art-prompts.md",
        char_dir / "sprites" / "art-prompts.md",
        char_dir / "reference" / "art-prompts.md",
    ]:
        if candidate.exists():
            art_prompts_path = candidate
            break

    if not art_prompts_path:
        print(f"[SKIP] {name}: art-prompts.md nao encontrado")
        return

    prompts = extract_prompts_from_md(art_prompts_path)
    if not prompts:
        print(f"[SKIP] {name}: nenhum prompt extraido")
        return

    print(f"\n🎨 {name.upper()} — {len(prompts)} frames para gerar")

    if dry_run:
        for p in prompts:
            print(f"  [{p['name'][:40]:40s}] prompt: {p['prompt'][:80]}...")
        return

    # Output dirs
    hires_dir = OUTPUT_DIR / name / "hires"
    pixel_dir = OUTPUT_DIR / name / "pixels"
    sheet_dir = OUTPUT_DIR / name
    hires_dir.mkdir(parents=True, exist_ok=True)
    pixel_dir.mkdir(parents=True, exist_ok=True)

    frame_size = (64, 64)  # Personagens
    frame_paths = []
    frame_names = []

    for i, p in enumerate(prompts):
        safe_name = re.sub(r'[^a-z0-9_-]', '_', p['name'].lower().strip())[:40]
        hires_path = hires_dir / f"{i:02d}_{safe_name}.png"
        pixel_path = pixel_dir / f"{i:02d}_{safe_name}.png"

        if hires_path.exists():
            print(f"  [SKIP] {safe_name} (ja existe)")
        else:
            print(f"  [GEN]  {safe_name}...")
            try:
                if engine == "dalle":
                    generate_dalle(p["prompt"], p["negative"], hires_path)
                elif engine == "stability":
                    generate_stability(p["prompt"], p["negative"], hires_path)
                time.sleep(1)  # Rate limit
            except Exception as e:
                print(f"  [ERRO] {safe_name}: {e}")
                continue

        # Downscale para pixel art
        if hires_path.exists():
            downscale_nearest(hires_path, pixel_path, frame_size)
            frame_paths.append(pixel_path)
            frame_names.append(f"{name}_{safe_name}")

    # Montar sprite sheet
    if frame_paths:
        sheet_path = sheet_dir / f"{name}_spritesheet.png"
        json_path = sheet_dir / f"{name}_atlas.json"
        create_sprite_sheet(frame_paths, sheet_path, frame_size)
        create_phaser_atlas_json(sheet_path, frame_names, frame_size, json_path)


def process_weapon(name: str, engine: str, dry_run: bool = False):
    """Processa sprites de uma arma."""
    weapon_dir = ARMAS_DIR / name

    art_prompts_path = None
    for candidate in [
        weapon_dir / "art-prompts.md",
        weapon_dir / "sprites" / "art-prompts.md",
    ]:
        if candidate.exists():
            art_prompts_path = candidate
            break

    if not art_prompts_path:
        return

    prompts = extract_prompts_from_md(art_prompts_path)
    if not prompts:
        return

    print(f"\n⚔️  {name.upper()} — {len(prompts)} frames")

    if dry_run:
        for p in prompts:
            print(f"  [{p['name'][:40]:40s}] prompt: {p['prompt'][:80]}...")
        return

    hires_dir = OUTPUT_DIR / "armas" / name / "hires"
    pixel_dir = OUTPUT_DIR / "armas" / name / "pixels"
    hires_dir.mkdir(parents=True, exist_ok=True)
    pixel_dir.mkdir(parents=True, exist_ok=True)

    frame_size = (32, 32)  # Armas sao menores
    frame_paths = []
    frame_names = []

    for i, p in enumerate(prompts):
        safe_name = re.sub(r'[^a-z0-9_-]', '_', p['name'].lower().strip())[:40]
        hires_path = hires_dir / f"{i:02d}_{safe_name}.png"
        pixel_path = pixel_dir / f"{i:02d}_{safe_name}.png"

        if not hires_path.exists():
            print(f"  [GEN]  {safe_name}...")
            try:
                if engine == "dalle":
                    generate_dalle(p["prompt"], p["negative"], hires_path)
                elif engine == "stability":
                    generate_stability(p["prompt"], p["negative"], hires_path)
                time.sleep(1)
            except Exception as e:
                print(f"  [ERRO] {safe_name}: {e}")
                continue

        if hires_path.exists():
            downscale_nearest(hires_path, pixel_path, frame_size)
            frame_paths.append(pixel_path)
            frame_names.append(f"weapon_{name}_{safe_name}")

    if frame_paths:
        sheet_path = OUTPUT_DIR / "armas" / name / f"{name}_spritesheet.png"
        json_path = OUTPUT_DIR / "armas" / name / f"{name}_atlas.json"
        create_sprite_sheet(frame_paths, sheet_path, frame_size)
        create_phaser_atlas_json(sheet_path, frame_names, frame_size, json_path)


def main():
    parser = argparse.ArgumentParser(description="Gera sprites para Zumbis de Brasilia")
    parser.add_argument("--engine", choices=["dalle", "stability"], default="dalle",
                        help="Engine de geracao de imagem")
    parser.add_argument("--personagem", "-p", help="Gerar sprites de um personagem especifico")
    parser.add_argument("--armas", action="store_true", help="Gerar sprites de armas")
    parser.add_argument("--all", action="store_true", help="Gerar TUDO")
    parser.add_argument("--dry-run", action="store_true", help="Mostra prompts sem gerar")
    args = parser.parse_args()

    print("🧟 ZUMBIS DE BRASILIA — Sprite Generation Pipeline")
    print(f"   Engine: {args.engine}")
    print(f"   Output: {OUTPUT_DIR}")
    print()

    if args.personagem:
        process_character(args.personagem, args.engine, args.dry_run)
    elif args.armas:
        for weapon_dir in sorted(ARMAS_DIR.iterdir()):
            if weapon_dir.is_dir():
                process_weapon(weapon_dir.name, args.engine, args.dry_run)
    elif args.all:
        # Personagens
        for char_dir in sorted(PERSONAGENS_DIR.iterdir()):
            if char_dir.is_dir():
                process_character(char_dir.name, args.engine, args.dry_run)
        # Armas
        for weapon_dir in sorted(ARMAS_DIR.iterdir()):
            if weapon_dir.is_dir():
                process_weapon(weapon_dir.name, args.engine, args.dry_run)
    else:
        parser.print_help()
        print("\n📋 Personagens disponiveis:")
        for d in sorted(PERSONAGENS_DIR.iterdir()):
            if d.is_dir():
                has_prompts = any((d / f).exists() for f in ["art-prompts.md", "sprites/art-prompts.md"])
                status = "✅" if has_prompts else "❌ (sem art-prompts)"
                print(f"   {status} {d.name}")


if __name__ == "__main__":
    main()
