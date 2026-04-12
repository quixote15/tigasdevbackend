#!/usr/bin/env python3
"""
Parseia arquivos de legenda VTT/SRT e gera transcrições limpas em texto.
Remove timestamps, tags HTML e duplicatas de linhas.

Uso:
    python3 02_parse_transcricoes.py
"""

import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
TRANSCRICOES_DIR = BASE_DIR / "transcricoes"
TRANSCRICOES_CLEAN_DIR = BASE_DIR / "transcricoes_limpas"


def parse_vtt(filepath: Path) -> str:
    """Parseia arquivo VTT e retorna texto limpo."""
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    lines = content.split("\n")

    text_lines = []
    seen = set()

    for line in lines:
        line = line.strip()
        # Pular headers VTT
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        # Pular linhas de timestamp
        if re.match(r"^\d{2}:\d{2}", line) or re.match(r"^[\d:.]+\s*-->", line):
            continue
        # Pular linhas vazias e números de sequência
        if not line or re.match(r"^\d+$", line):
            continue
        # Pular tags de posicionamento
        if line.startswith("align:") or line.startswith("position:"):
            continue

        # Limpar tags HTML
        clean = re.sub(r"<[^>]+>", "", line)
        clean = re.sub(r"\[.*?\]", "", clean)  # Remove [Music], [Applause], etc.
        clean = clean.strip()

        if not clean:
            continue

        # Deduplicar (VTT repete linhas em blocos sobrepostos)
        if clean not in seen:
            seen.add(clean)
            text_lines.append(clean)

    return " ".join(text_lines)


def parse_srt(filepath: Path) -> str:
    """Parseia arquivo SRT e retorna texto limpo."""
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    lines = content.split("\n")

    text_lines = []
    seen = set()

    for line in lines:
        line = line.strip()
        if re.match(r"^\d+$", line):
            continue
        if re.match(r"^\d{2}:\d{2}", line):
            continue
        if not line:
            continue

        clean = re.sub(r"<[^>]+>", "", line)
        clean = re.sub(r"\[.*?\]", "", clean)
        clean = clean.strip()

        if clean and clean not in seen:
            seen.add(clean)
            text_lines.append(clean)

    return " ".join(text_lines)


def main():
    TRANSCRICOES_CLEAN_DIR.mkdir(parents=True, exist_ok=True)

    # Encontrar todos os arquivos de legenda
    sub_files = list(TRANSCRICOES_DIR.glob("*.vtt")) + list(TRANSCRICOES_DIR.glob("*.srt"))

    if not sub_files:
        print("❌ Nenhum arquivo de legenda encontrado em transcricoes/")
        print("   Execute primeiro: python3 01_download_videos.py --only-subs")
        return

    print(f"📝 Encontrados {len(sub_files)} arquivos de legenda")

    all_transcriptions = {}

    for sub_file in sorted(sub_files):
        video_id = sub_file.stem.replace(".pt", "")

        # Carregar metadados se disponível
        meta_file = TRANSCRICOES_DIR / f"{video_id}.json"
        title = video_id
        if meta_file.exists():
            meta = json.loads(meta_file.read_text())
            title = meta.get("title", video_id)

        # Parsear
        if sub_file.suffix == ".vtt":
            text = parse_vtt(sub_file)
        else:
            text = parse_srt(sub_file)

        if not text or len(text) < 50:
            print(f"  ⚠️  Transcrição muito curta ou vazia: {title}")
            continue

        # Salvar transcrição limpa individual
        clean_file = TRANSCRICOES_CLEAN_DIR / f"{video_id}.txt"
        clean_file.write_text(f"# {title}\n\n{text}\n", encoding="utf-8")

        all_transcriptions[video_id] = {
            "title": title,
            "text": text,
            "word_count": len(text.split()),
        }

        print(f"  ✅ {title} ({len(text.split())} palavras)")

    # Salvar compilado
    compiled = TRANSCRICOES_CLEAN_DIR / "_todas_transcricoes.json"
    compiled.write_text(json.dumps(all_transcriptions, ensure_ascii=False, indent=2))

    # Salvar texto corrido (para análise rápida)
    all_text_file = TRANSCRICOES_CLEAN_DIR / "_todas_transcricoes.txt"
    all_text = ""
    for vid_id, data in all_transcriptions.items():
        all_text += f"\n{'='*60}\n# {data['title']}\n{'='*60}\n\n{data['text']}\n"
    all_text_file.write_text(all_text, encoding="utf-8")

    total_words = sum(d["word_count"] for d in all_transcriptions.values())
    print(f"\n✅ Concluído!")
    print(f"   {len(all_transcriptions)} transcrições parseadas")
    print(f"   {total_words:,} palavras totais")
    print(f"   Transcrições limpas: {TRANSCRICOES_CLEAN_DIR}")
    print(f"   Compilado JSON: {compiled}")
    print(f"   Compilado TXT: {all_text_file}")


if __name__ == "__main__":
    main()
