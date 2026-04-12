#!/usr/bin/env python3
"""
Download videos e transcrições do canal André Guedes (Zumbis de Brasília).
Usa yt-dlp para baixar vídeos + legendas auto-geradas em português.

Uso:
    python3 01_download_videos.py [--only-subs] [--limit N] [--search TERMO]
"""

import subprocess
import sys
import json
import os
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).parent
VIDEOS_DIR = BASE_DIR / "videos"
TRANSCRICOES_DIR = BASE_DIR / "transcricoes"

CHANNEL_URL = "https://www.youtube.com/@AndreGuedesCartoon"

# Playlists e buscas conhecidas de sátira política
SEARCH_QUERIES = [
    # Canal principal - todos os vídeos
    f"{CHANNEL_URL}/videos",
    # Buscas específicas para conteúdo de sátira
    "ytsearch50:André Guedes Zumbis em Brasília",
    "ytsearch30:André Guedes Limbo dos Cancelados",
    "ytsearch30:André Guedes sátira política animação",
    "ytsearch20:André Guedes eleições cartoon",
    "ytsearch20:André Guedes congresso zumbi",
]

# Flag global para SSL (redes corporativas/proxy)
NO_CHECK_CERT = True


def run_yt_dlp(args: list[str], capture=False) -> subprocess.CompletedProcess:
    cmd = ["yt-dlp", "--no-check-certificates"] + args
    print(f"  → {' '.join(cmd[:6])}...")
    return subprocess.run(cmd, capture_output=capture, text=True)


def get_video_list(url: str, limit: int | None = None) -> list[dict]:
    """Lista vídeos de uma URL/playlist sem baixar."""
    args = [
        "--flat-playlist",
        "--dump-json",
        "--no-warnings",
        "--ignore-errors",
    ]
    if limit:
        args += ["--playlist-end", str(limit)]
    args.append(url)

    result = run_yt_dlp(args, capture=True)
    videos = []
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            data = json.loads(line)
            videos.append({
                "id": data.get("id", ""),
                "title": data.get("title", ""),
                "url": data.get("url", data.get("webpage_url", f"https://www.youtube.com/watch?v={data.get('id', '')}")),
                "duration": data.get("duration"),
                "view_count": data.get("view_count"),
                "upload_date": data.get("upload_date"),
            })
        except json.JSONDecodeError:
            continue
    return videos


def filter_satire_videos(videos: list[dict]) -> list[dict]:
    """Filtra apenas vídeos de sátira política."""
    keywords = [
        "zumbi", "brasilia", "brasília", "congresso", "político", "politico",
        "eleição", "eleicao", "presidente", "deputado", "senador", "ministro",
        "cancelado", "limbo", "stf", "planalto", "lula", "bolsonaro",
        "corrupção", "corrupcao", "cpi", "impeachment", "votação", "votacao",
        "campanha", "partido", "esquerda", "direita", "governo", "oposição",
        "oposicao", "sátira", "satira", "política", "politica",
    ]
    filtered = []
    seen_ids = set()
    for v in videos:
        if v["id"] in seen_ids:
            continue
        title_lower = v.get("title", "").lower()
        if any(kw in title_lower for kw in keywords):
            filtered.append(v)
            seen_ids.add(v["id"])
    return filtered


def download_video_and_subs(video: dict, only_subs: bool = False):
    """Baixa vídeo e/ou legendas."""
    video_id = video["id"]
    title = video.get("title", video_id)
    url = video.get("url", f"https://www.youtube.com/watch?v={video_id}")

    # Arquivo de transcrição
    sub_path = TRANSCRICOES_DIR / f"{video_id}.pt.vtt"
    sub_json = TRANSCRICOES_DIR / f"{video_id}.json"

    # Salvar metadados
    if not sub_json.exists():
        sub_json.write_text(json.dumps(video, ensure_ascii=False, indent=2))

    # Baixar legendas (auto-geradas em pt)
    if not sub_path.exists() and not (TRANSCRICOES_DIR / f"{video_id}.pt.srt").exists():
        print(f"\n📝 Baixando legendas: {title}")
        sub_args = [
            "--write-auto-sub",
            "--write-sub",
            "--sub-lang", "pt",
            "--sub-format", "vtt/srt/best",
            "--skip-download",
            "--no-warnings",
            "--ignore-errors",
            "-o", str(TRANSCRICOES_DIR / f"{video_id}.%(ext)s"),
            url,
        ]
        run_yt_dlp(sub_args)

    # Baixar vídeo (720p max para economizar espaço)
    if not only_subs:
        video_path = VIDEOS_DIR / f"{video_id}.mp4"
        if not video_path.exists():
            print(f"\n🎬 Baixando vídeo: {title}")
            vid_args = [
                "-f", "bestvideo[height<=720]+bestaudio/best[height<=720]",
                "--merge-output-format", "mp4",
                "--no-warnings",
                "--ignore-errors",
                "-o", str(video_path),
                url,
            ]
            run_yt_dlp(vid_args)


def main():
    parser = argparse.ArgumentParser(description="Download vídeos André Guedes")
    parser.add_argument("--only-subs", action="store_true",
                        help="Baixar apenas legendas/transcrições, sem vídeos")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limitar número de vídeos por fonte")
    parser.add_argument("--search", type=str, default=None,
                        help="Termo de busca personalizado")
    parser.add_argument("--list-only", action="store_true",
                        help="Apenas listar vídeos encontrados, sem baixar")
    args = parser.parse_args()

    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    TRANSCRICOES_DIR.mkdir(parents=True, exist_ok=True)

    queries = SEARCH_QUERIES
    if args.search:
        queries = [f"ytsearch50:{args.search}"]

    # Coletar todos os vídeos
    all_videos = []
    for query in queries:
        print(f"\n🔍 Buscando: {query[:80]}...")
        videos = get_video_list(query, limit=args.limit)
        print(f"   Encontrados: {len(videos)} vídeos")
        all_videos.extend(videos)

    # Filtrar sátira
    satire_videos = filter_satire_videos(all_videos)
    print(f"\n{'='*60}")
    print(f"Total encontrado: {len(all_videos)} vídeos")
    print(f"Filtrado (sátira): {len(satire_videos)} vídeos")
    print(f"{'='*60}")

    if args.list_only:
        for i, v in enumerate(satire_videos, 1):
            dur = f"{v['duration']//60}:{v['duration']%60:02d}" if v.get("duration") else "?"
            views = f"{v.get('view_count', 0):,}" if v.get("view_count") else "?"
            print(f"  {i:3d}. [{dur}] {v['title']} ({views} views)")
        return

    # Salvar lista completa
    manifest = BASE_DIR / "video_manifest.json"
    manifest.write_text(json.dumps(satire_videos, ensure_ascii=False, indent=2))
    print(f"\n📋 Manifesto salvo em: {manifest}")

    # Baixar
    for i, video in enumerate(satire_videos, 1):
        print(f"\n[{i}/{len(satire_videos)}] {video['title']}")
        try:
            download_video_and_subs(video, only_subs=args.only_subs)
        except Exception as e:
            print(f"   ❌ Erro: {e}")
            continue

    print(f"\n✅ Concluído!")
    print(f"   Vídeos: {VIDEOS_DIR}")
    print(f"   Transcrições: {TRANSCRICOES_DIR}")


if __name__ == "__main__":
    main()
