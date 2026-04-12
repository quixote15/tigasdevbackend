#!/usr/bin/env python3
"""
ZUMBIS DE BRASILIA — Extrator de Vozes do Andre Guedes

Pipeline para extrair as vozes REAIS dos personagens dos videos do Andre Guedes.
Ele usa vozes distintas por personagem — precisamos extrair os clips de audio
onde cada personagem fala seus bordoes.

PIPELINE:
  1. Baixa audio dos videos (yt-dlp, so audio)
  2. Usa as transcricoes VTT (com timestamps) para localizar bordoes
  3. Recorta clips de audio nos timestamps corretos (ffmpeg)
  4. Organiza por personagem
  5. (Opcional) Clona voz via ElevenLabs para gerar novos bordoes

Uso:
    # Passo 1: Baixar audio de videos que mencionam um personagem
    python 04_extrair_vozes.py --baixar --personagem lula --limit 10

    # Passo 2: Extrair clips dos bordoes
    python 04_extrair_vozes.py --extrair --personagem lula

    # Passo 3: Clonar voz e gerar novos bordoes (requer ELEVENLABS_API_KEY)
    python 04_extrair_vozes.py --clonar --personagem lula

    # Tudo de uma vez:
    python 04_extrair_vozes.py --pipeline --personagem daciolo --limit 5

    # Listar bordoes encontrados nas transcricoes:
    python 04_extrair_vozes.py --buscar --personagem xandao

Dependencias:
    pip install yt-dlp elevenlabs
    brew install ffmpeg  (ou apt install ffmpeg)
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from dataclasses import dataclass, field

BASE_DIR = Path(__file__).parent
PROJECT_DIR = BASE_DIR.parent
ASSETS_DIR = PROJECT_DIR / "assets"
TRANSCRICOES_DIR = BASE_DIR / "transcricoes"
TRANSCRICOES_LIMPAS_DIR = BASE_DIR / "transcricoes_limpas"
VIDEOS_DIR = BASE_DIR / "videos"
AUDIO_DIR = BASE_DIR / "audio_extraido"
MANIFEST_PATH = BASE_DIR / "video_manifest.json"
CLIPS_DIR = ASSETS_DIR / "audio" / "bordoes" / "clips_reais"

# Bordoes por personagem — termos de busca nas transcricoes
# (lowercase, sem acentos para matching flexivel)
BORDOES_BUSCA: dict[str, list[dict]] = {
    "lula": [
        {"texto": "companheiro", "contexto": "eu quero dizer pra vocês", "id": "lula-01"},
        {"texto": "álcool em mim", "contexto": "companheiro álcool", "id": "lula-02"},
        {"texto": "tá maravilhoso", "contexto": "maravilhoso", "id": "lula-03"},
        {"texto": "culpa é do bolsonaro", "contexto": "culpa", "id": "lula-04"},
        {"texto": "nunca antes na história", "contexto": "nunca antes", "id": "lula-05"},
        {"texto": "faz o l", "contexto": "faz o l", "id": "lula-06"},
        {"texto": "fico puto", "contexto": "puto da vida", "id": "lula-07"},
        {"texto": "a gente vamos", "contexto": "a gente vamos", "id": "lula-08"},
        {"texto": "velho barreiro", "contexto": "velho barreiro", "id": "lula-09"},
    ],
    "bolsonaro": [
        {"texto": "talkei", "contexto": "tá ok", "id": "bolso-01"},
        {"texto": "bomba", "contexto": "bomba", "id": "bolso-02"},
        {"texto": "vagabundo", "contexto": "vagabundo canalha", "id": "bolso-03"},
        {"texto": "e daí", "contexto": "e daí lamento", "id": "bolso-04"},
        {"texto": "gripezinha", "contexto": "gripezinha", "id": "bolso-05"},
        {"texto": "imbrochável", "contexto": "imbrochável", "id": "bolso-06"},
        {"texto": "pintou um clima", "contexto": "pintou", "id": "bolso-07"},
        {"texto": "brochável", "contexto": "arma brochável", "id": "bolso-08"},
    ],
    "daciolo": [
        {"texto": "glória a deus", "contexto": "glória", "id": "daci-01"},
        {"texto": "queima jesus", "contexto": "queima", "id": "daci-02"},
        {"texto": "cheiro de satanás", "contexto": "satanás", "id": "daci-03"},
        {"texto": "ursal", "contexto": "ursal", "id": "daci-04"},
        {"texto": "glória a sap", "contexto": "sap", "id": "daci-05"},
    ],
    "xandao": [
        {"texto": "monocraticamente", "contexto": "monocraticamente", "id": "xand-01"},
        {"texto": "faz silêncio", "contexto": "silêncio", "id": "xand-02"},
        {"texto": "censurado", "contexto": "censurado", "id": "xand-03"},
        {"texto": "xandaquistão", "contexto": "xandaquistão", "id": "xand-04"},
    ],
    "ciro": [
        {"texto": "rivotril", "contexto": "acabou meu rivotril", "id": "ciro-01"},
        {"texto": "bossaloide", "contexto": "bossaloide", "id": "ciro-02"},
        {"texto": "paçoca", "contexto": "paçoca", "id": "ciro-03"},
        {"texto": "terceira via", "contexto": "terceira via", "id": "ciro-04"},
        {"texto": "que brisa", "contexto": "que brisa mano", "id": "ciro-05"},
    ],
    "gilmar": [
        {"texto": "sou fã", "contexto": "sou fã sou fã", "id": "gilm-01"},
        {"texto": "vagabundo", "contexto": "vagabundo vagabundo", "id": "gilm-02"},
        {"texto": "pastel", "contexto": "pastel", "id": "gilm-03"},
    ],
    "taxadd": [
        {"texto": "taxado", "contexto": "taxado", "id": "taxa-01"},
        {"texto": "merenda", "contexto": "que horas é a merenda", "id": "taxa-02"},
    ],
    "trump": [
        {"texto": "tremendous", "contexto": "tremendous", "id": "trump-01"},
        {"texto": "fake news", "contexto": "fake news", "id": "trump-02"},
    ],
    "eneas": [
        {"texto": "meu nome é enéas", "contexto": "enéas", "id": "eneas-01"},
        {"texto": "cinquenta e seis", "contexto": "cinquenta e seis", "id": "eneas-02"},
    ],
    "eduardo": [
        {"texto": "pai", "contexto": "pai pai", "id": "edu-01"},
        {"texto": "embaixada", "contexto": "embaixada", "id": "edu-02"},
        {"texto": "bananinha", "contexto": "bananinha", "id": "edu-03"},
    ],
    "janja": [
        {"texto": "fora elon", "contexto": "fora elon musk", "id": "janja-01"},
        {"texto": "quem manda", "contexto": "quem manda aqui", "id": "janja-02"},
    ],
    "monark": [
        {"texto": "mano pensa comigo", "contexto": "pensa comigo", "id": "monark-01"},
        {"texto": "limbo", "contexto": "bem-vindo ao limbo", "id": "monark-02"},
    ],
}


@dataclass
class VTTSegment:
    """Um segmento de legenda VTT com timestamps."""
    start: float  # segundos
    end: float    # segundos
    text: str
    video_id: str = ""


def parse_vtt_timestamps(vtt_path: Path) -> list[VTTSegment]:
    """Parse arquivo VTT e retorna segmentos com timestamps em segundos."""
    if not vtt_path.exists():
        return []

    content = vtt_path.read_text(encoding="utf-8", errors="replace")
    segments = []

    # Pattern VTT: 00:00:01.234 --> 00:00:04.567 (com atributos opcionais como align:start)
    pattern = re.compile(
        r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})[^\n]*\n(.+?)(?=\n\n|\n\d{2}:\d{2}|\Z)',
        re.DOTALL
    )

    video_id = vtt_path.stem.replace(".pt", "")

    for match in pattern.finditer(content):
        start_str, end_str, text = match.groups()
        start = _ts_to_seconds(start_str)
        end = _ts_to_seconds(end_str)
        # Limpar tags <c>, <>, posicoes e linhas vazias
        text = re.sub(r'<\d{2}:\d{2}:\d{2}\.\d{3}>', ' ', text)  # timestamps inline
        text = re.sub(r'</?c>', '', text)  # tags <c>
        text = re.sub(r'<[^>]+>', '', text)  # qualquer outra tag HTML
        text = re.sub(r'align:\S+', '', text)
        text = re.sub(r'position:\d+%\S*', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        if text and len(text) > 2:
            segments.append(VTTSegment(start=start, end=end, text=text, video_id=video_id))

    # Deduplicar segmentos consecutivos com mesmo texto (VTT repete linhas)
    deduped = []
    for seg in segments:
        if not deduped or seg.text != deduped[-1].text:
            deduped.append(seg)
        else:
            # Extender o end do segmento anterior
            deduped[-1].end = max(deduped[-1].end, seg.end)

    return deduped


def _ts_to_seconds(ts: str) -> float:
    """Converte timestamp HH:MM:SS.mmm para segundos."""
    parts = ts.split(":")
    h, m = int(parts[0]), int(parts[1])
    s = float(parts[2])
    return h * 3600 + m * 60 + s


def buscar_bordoes_em_transcricoes(personagem: str) -> list[dict]:
    """Busca bordoes de um personagem em todas as transcricoes VTT."""
    bordoes = BORDOES_BUSCA.get(personagem, [])
    if not bordoes:
        print(f"[WARN] Nenhum bordao cadastrado para '{personagem}'")
        return []

    resultados = []
    vtt_files = sorted(TRANSCRICOES_DIR.glob("*.vtt"))
    print(f"Buscando bordoes de {personagem} em {len(vtt_files)} transcricoes...")

    for vtt_path in vtt_files:
        segments = parse_vtt_timestamps(vtt_path)
        if not segments:
            continue

        for bordao in bordoes:
            termo = bordao["texto"].lower()
            for seg in segments:
                if termo in seg.text.lower():
                    resultados.append({
                        "bordao_id": bordao["id"],
                        "bordao_texto": bordao["texto"],
                        "video_id": seg.video_id,
                        "start": seg.start,
                        "end": seg.end,
                        "transcricao": seg.text,
                        "vtt_file": str(vtt_path.name),
                    })

    # Deduplicar por video_id + bordao_id (manter primeiro de cada)
    seen = set()
    deduped = []
    for r in resultados:
        key = (r["video_id"], r["bordao_id"])
        if key not in seen:
            seen.add(key)
            deduped.append(r)

    print(f"Encontrados {len(deduped)} clips ({len(resultados)} total com duplicatas)")
    return deduped


def baixar_audio_video(video_id: str) -> Path:
    """Baixa apenas o audio de um video do YouTube via yt-dlp."""
    audio_dir = AUDIO_DIR / video_id
    audio_dir.mkdir(parents=True, exist_ok=True)
    audio_path = audio_dir / f"{video_id}.mp3"

    if audio_path.exists():
        print(f"  [SKIP] Audio ja existe: {video_id}")
        return audio_path

    print(f"  [DL] Baixando audio: {video_id}...")
    url = f"https://www.youtube.com/watch?v={video_id}"

    try:
        subprocess.run([
            "yt-dlp",
            "--no-check-certificates",
            "-x", "--audio-format", "mp3",
            "--audio-quality", "192K",
            "-o", str(audio_path),
            "--no-playlist",
            url,
        ], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"  [ERRO] Falha ao baixar {video_id}: {e.stderr[:200]}")
        return audio_path
    except FileNotFoundError:
        print("  [ERRO] yt-dlp nao encontrado. Instale: pip install yt-dlp")
        sys.exit(1)

    return audio_path


def recortar_clip(audio_path: Path, start: float, end: float, output_path: Path,
                  padding: float = 0.5) -> bool:
    """Recorta um trecho do audio usando ffmpeg."""
    if not audio_path.exists():
        return False

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Adicionar padding antes e depois para pegar o contexto
    adj_start = max(0, start - padding)
    duration = (end - start) + (padding * 2)

    try:
        subprocess.run([
            "ffmpeg", "-y",
            "-ss", str(adj_start),
            "-t", str(duration),
            "-i", str(audio_path),
            "-c:a", "libmp3lame", "-q:a", "2",
            str(output_path),
        ], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERRO] ffmpeg falhou: {e.stderr[:200]}")
        return False
    except FileNotFoundError:
        print("  [ERRO] ffmpeg nao encontrado. Instale: brew install ffmpeg")
        return False


def clonar_voz_elevenlabs(clips_dir: Path, personagem: str, novos_bordoes: list[str]) -> list[Path]:
    """
    Clona a voz do personagem usando ElevenLabs a partir dos clips extraidos.
    Gera novos bordoes com a voz clonada.

    Requer: ELEVENLABS_API_KEY no ambiente.
    """
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("[ERRO] ELEVENLABS_API_KEY nao definida. Defina com:")
        print("  export ELEVENLABS_API_KEY='sua-chave-aqui'")
        print("  Obtenha em: https://elevenlabs.io/")
        return []

    try:
        from elevenlabs.client import ElevenLabs
        from elevenlabs import Voice, VoiceSettings
    except ImportError:
        print("[ERRO] elevenlabs nao instalado. Execute: pip install elevenlabs")
        return []

    client = ElevenLabs(api_key=api_key)

    # Pegar os melhores clips para treinamento (ate 25 clips, max 5 min total)
    clips = sorted(clips_dir.glob("*.mp3"))[:25]
    if len(clips) < 3:
        print(f"[WARN] Poucos clips ({len(clips)}) para clonagem de qualidade. Minimo recomendado: 3")
        if len(clips) == 0:
            return []

    print(f"\n🎤 Clonando voz de '{personagem}' com {len(clips)} clips...")

    # Criar voz clonada via Instant Voice Cloning
    voice = client.clone(
        name=f"zumbis-{personagem}",
        description=f"Voz do personagem {personagem} no estilo Andre Guedes - Zumbis de Brasilia",
        files=[str(c) for c in clips],
    )

    print(f"  Voz clonada criada: {voice.voice_id}")

    # Gerar novos bordoes
    output_dir = CLIPS_DIR / personagem / "clonados"
    output_dir.mkdir(parents=True, exist_ok=True)
    generated = []

    for i, texto in enumerate(novos_bordoes):
        output_path = output_dir / f"{personagem}-clone-{i:02d}.mp3"
        print(f"  [GEN] \"{texto[:50]}...\"")

        audio = client.generate(
            text=texto,
            voice=Voice(
                voice_id=voice.voice_id,
                settings=VoiceSettings(
                    stability=0.5,
                    similarity_boost=0.8,
                    style=0.3,
                )
            ),
            model_id="eleven_multilingual_v2",
        )

        with open(output_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        generated.append(output_path)
        print(f"  [OK] -> {output_path.name}")

    return generated


def pipeline_completo(personagem: str, limit: int = 10):
    """Pipeline completo: buscar -> baixar -> recortar -> (clonar)."""

    print(f"\n{'='*60}")
    print(f"  PIPELINE: {personagem.upper()}")
    print(f"{'='*60}\n")

    # 1. Buscar bordoes nas transcricoes
    print("PASSO 1: Buscando bordoes nas transcricoes...\n")
    resultados = buscar_bordoes_em_transcricoes(personagem)

    if not resultados:
        print(f"Nenhum bordao encontrado para '{personagem}' nas transcricoes.")
        return

    # Mostrar resultados
    for r in resultados[:20]:
        print(f"  [{r['bordao_id']}] \"{r['transcricao'][:60]}\" @ {r['start']:.1f}s-{r['end']:.1f}s ({r['video_id']})")

    # 2. Baixar audios (limitar quantidade)
    print(f"\nPASSO 2: Baixando audio de {min(limit, len(resultados))} videos...\n")
    video_ids = list(dict.fromkeys(r["video_id"] for r in resultados))[:limit]

    for vid_id in video_ids:
        baixar_audio_video(vid_id)

    # 3. Recortar clips
    print(f"\nPASSO 3: Recortando clips de bordoes...\n")
    clips_dir = CLIPS_DIR / personagem
    clips_dir.mkdir(parents=True, exist_ok=True)

    clips_gerados = 0
    for r in resultados:
        audio_path = AUDIO_DIR / r["video_id"] / f"{r['video_id']}.mp3"
        if not audio_path.exists():
            continue

        clip_name = f"{r['bordao_id']}_{r['video_id'][:8]}.mp3"
        clip_path = clips_dir / clip_name

        if clip_path.exists():
            clips_gerados += 1
            continue

        if recortar_clip(audio_path, r["start"], r["end"], clip_path):
            clips_gerados += 1
            print(f"  [CLIP] {clip_name} ({r['start']:.1f}s-{r['end']:.1f}s)")

    print(f"\n✅ {clips_gerados} clips extraidos para {personagem}")
    print(f"   Dir: {clips_dir}")

    # 4. Clonar voz (se API key disponivel)
    if os.getenv("ELEVENLABS_API_KEY"):
        print(f"\nPASSO 4: Clonando voz via ElevenLabs...\n")
        bordoes_config = BORDOES_BUSCA.get(personagem, [])
        textos = [b["contexto"] for b in bordoes_config]
        clonar_voz_elevenlabs(clips_dir, personagem, textos)
    else:
        print(f"\nPASSO 4: [SKIP] ELEVENLABS_API_KEY nao definida")
        print(f"   Para clonar a voz: export ELEVENLABS_API_KEY='sua-chave'")
        print(f"   Os clips reais extraidos podem ser usados diretamente no jogo!")


def main():
    parser = argparse.ArgumentParser(description="Extrai vozes reais do Andre Guedes")
    parser.add_argument("--personagem", "-p", required=True,
                        help=f"Personagem ({', '.join(BORDOES_BUSCA.keys())})")
    parser.add_argument("--limit", "-l", type=int, default=10,
                        help="Limite de videos para baixar (default: 10)")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--buscar", action="store_true", help="Buscar bordoes nas transcricoes")
    group.add_argument("--baixar", action="store_true", help="Baixar audio dos videos")
    group.add_argument("--extrair", action="store_true", help="Recortar clips dos bordoes")
    group.add_argument("--clonar", action="store_true", help="Clonar voz via ElevenLabs")
    group.add_argument("--pipeline", action="store_true", help="Pipeline completo")

    args = parser.parse_args()
    personagem = args.personagem.lower()

    if personagem not in BORDOES_BUSCA:
        print(f"Personagem '{personagem}' nao cadastrado.")
        print(f"Disponiveis: {', '.join(sorted(BORDOES_BUSCA.keys()))}")
        return

    if args.buscar:
        resultados = buscar_bordoes_em_transcricoes(personagem)
        print(f"\n{'='*60}")
        print(f"  BORDOES DE {personagem.upper()} ENCONTRADOS")
        print(f"{'='*60}")
        for r in resultados:
            print(f"  [{r['bordao_id']:10s}] \"{r['transcricao'][:50]}\" @ {r['start']:.1f}s ({r['video_id']})")
        print(f"\nTotal: {len(resultados)} ocorrencias")

    elif args.baixar:
        resultados = buscar_bordoes_em_transcricoes(personagem)
        video_ids = list(dict.fromkeys(r["video_id"] for r in resultados))[:args.limit]
        print(f"Baixando audio de {len(video_ids)} videos...")
        for vid_id in video_ids:
            baixar_audio_video(vid_id)

    elif args.extrair:
        resultados = buscar_bordoes_em_transcricoes(personagem)
        clips_dir = CLIPS_DIR / personagem
        clips_dir.mkdir(parents=True, exist_ok=True)
        for r in resultados:
            audio_path = AUDIO_DIR / r["video_id"] / f"{r['video_id']}.mp3"
            if not audio_path.exists():
                print(f"  [SKIP] Audio nao baixado: {r['video_id']}")
                continue
            clip_name = f"{r['bordao_id']}_{r['video_id'][:8]}.mp3"
            clip_path = clips_dir / clip_name
            if recortar_clip(audio_path, r["start"], r["end"], clip_path):
                print(f"  [OK] {clip_name}")

    elif args.clonar:
        clips_dir = CLIPS_DIR / personagem
        if not clips_dir.exists() or not list(clips_dir.glob("*.mp3")):
            print(f"Nenhum clip encontrado em {clips_dir}. Execute --extrair primeiro.")
            return
        bordoes_config = BORDOES_BUSCA.get(personagem, [])
        textos = [b["contexto"] for b in bordoes_config]
        clonar_voz_elevenlabs(clips_dir, personagem, textos)

    elif args.pipeline:
        pipeline_completo(personagem, args.limit)


if __name__ == "__main__":
    main()
