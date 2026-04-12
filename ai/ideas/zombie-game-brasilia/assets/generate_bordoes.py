#!/usr/bin/env python3
"""
ZUMBIS DE BRASILIA — Gerador de Audio (Bordoes)
Usa edge-tts (Microsoft Azure) para gerar MP3 dos bordoes de cada personagem.
Tambem gera OGG via ffmpeg para compatibilidade Phaser 3.

Uso:
    pip install edge-tts
    python generate_bordoes.py                    # Gera todos
    python generate_bordoes.py --personagem lula  # Gera so um
    python generate_bordoes.py --list-voices      # Lista vozes PT-BR

Formatos de saida:
    - MP3 (compatibilidade geral)
    - OGG (melhor para web/Phaser 3)
"""

import asyncio
import json
import os
import ssl
import subprocess
import sys
from pathlib import Path
from dataclasses import dataclass

# Bypass SSL para ambientes com proxy corporativo (Netskope, etc.)
ssl._create_default_https_context = ssl._create_unverified_context
os.environ["PYTHONHTTPSVERIFY"] = "0"

# Patch edge-tts internal SSL context (usa _SSL_CTX no ws_connect)
try:
    from edge_tts import communicate as _edge_communicate
    _ssl_ctx = ssl.create_default_context()
    _ssl_ctx.check_hostname = False
    _ssl_ctx.verify_mode = ssl.CERT_NONE
    _edge_communicate._SSL_CTX = _ssl_ctx
except Exception:
    pass

# ─── Configuracao ───

BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio" / "bordoes" / "generated"
MANIFEST_PATH = BASE_DIR / "audio" / "bordoes" / "manifest.json"

# Vozes PT-BR disponiveis no edge-tts
VOICES = {
    "masculina_grave": "pt-BR-AntonioNeural",      # Lula, Bolsonaro, Gilmar, Moro
    "masculina_aguda": "pt-BR-AntonioNeural",       # Daciolo, Ciro (ajustar pitch)
    "feminina": "pt-BR-FranciscaNeural",            # Janja, Marina
    "masculina_default": "pt-BR-AntonioNeural",     # Default
}


@dataclass
class Bordao:
    personagem: str
    id: str
    texto: str
    trigger: str  # idle, attack, death, spawn, special
    emocao: str
    volume: int  # 1-10
    voice: str
    rate: str  # ex: "+10%", "-5%"
    pitch: str  # ex: "+5Hz", "-2Hz"
    duracao_estimada: float  # segundos


# ─── CATALOGO DE BORDOES ───
# Extraido dos specs gerados pelos agentes de arte

BORDOES: list[Bordao] = [
    # ── LULA ──
    Bordao("lula", "lula-01", "Eu quero dizer pra vocês...", "idle", "pomposo", 6, "masculina_grave", "-5%", "-2Hz", 2.0),
    Bordao("lula", "lula-02", "Companheiro álcool em mim!", "attack", "animado", 8, "masculina_grave", "+5%", "+0Hz", 1.8),
    Bordao("lula", "lula-03", "Tá maravilhoso, companheiro!", "idle", "entusiasmado", 7, "masculina_grave", "+10%", "+2Hz", 2.0),
    Bordao("lula", "lula-04", "A culpa é do Bolsonaro!", "hit", "indignado", 9, "masculina_grave", "+15%", "+3Hz", 1.5),
    Bordao("lula", "lula-05", "Nunca antes na história deste país...", "special", "grandioso", 8, "masculina_grave", "-10%", "-3Hz", 2.5),
    Bordao("lula", "lula-06", "Faz o L!", "attack", "animado", 9, "masculina_grave", "+10%", "+5Hz", 0.8),
    Bordao("lula", "lula-07", "Fico puto da vida!", "hit", "raiva", 10, "masculina_grave", "+20%", "+5Hz", 1.2),
    Bordao("lula", "lula-08", "A gente vamos...", "walk", "casual", 5, "masculina_grave", "+0%", "+0Hz", 1.0),
    Bordao("lula", "lula-09", "Essa cicatriz é do povo, companheiro.", "death", "dramatico", 6, "masculina_grave", "-15%", "-5Hz", 2.5),

    # ── BOLSONARO ──
    Bordao("bolsonaro", "bolso-01", "TALKEI?", "idle", "casual_agressivo", 7, "masculina_grave", "+10%", "+3Hz", 0.6),
    Bordao("bolsonaro", "bolso-02", "Bomba!", "attack", "excitado", 9, "masculina_grave", "+20%", "+5Hz", 0.5),
    Bordao("bolsonaro", "bolso-03", "Vagabundo! Canalha!", "hit", "raiva", 10, "masculina_grave", "+15%", "+5Hz", 1.5),
    Bordao("bolsonaro", "bolso-04", "E daí? Lamento. Quer que eu faça o quê?", "death", "desdenho", 6, "masculina_grave", "+0%", "+0Hz", 2.5),
    Bordao("bolsonaro", "bolso-05", "É só uma gripezinha!", "idle", "deboche", 7, "masculina_grave", "+5%", "+2Hz", 1.5),
    Bordao("bolsonaro", "bolso-06", "Imbrochável!", "special", "orgulho", 9, "masculina_grave", "+10%", "+5Hz", 1.0),
    Bordao("bolsonaro", "bolso-07", "Pintou um clima...", "special", "constrangido", 5, "masculina_grave", "-10%", "-2Hz", 1.5),
    Bordao("bolsonaro", "bolso-08", "Minha arma é brochável!", "attack_fail", "frustrado", 8, "masculina_grave", "+5%", "+0Hz", 1.5),

    # ── DACIOLO ──
    Bordao("daciolo", "daci-01a", "Glória a Deus...", "idle_safe", "devoto_sussurro", 3, "masculina_aguda", "-10%", "+0Hz", 1.0),
    Bordao("daciolo", "daci-01b", "GLÓRIA A DEUS!", "idle", "entusiasmado", 7, "masculina_aguda", "+5%", "+5Hz", 1.2),
    Bordao("daciolo", "daci-01c", "GLÓÓÓÓRIA A DEEEEEUS!", "special", "extase_cosmico", 10, "masculina_aguda", "+15%", "+8Hz", 2.5),
    Bordao("daciolo", "daci-02", "Queima, Jesus! Shabalabá!", "attack", "exorcismo", 9, "masculina_aguda", "+10%", "+5Hz", 2.0),
    Bordao("daciolo", "daci-03", "Sinto o cheiro de Satanás neste recinto!", "enemy_spawn", "alerta_divino", 8, "masculina_aguda", "+5%", "+3Hz", 2.5),
    Bordao("daciolo", "daci-04", "A URSAL! A URSAL EXISTE!", "ultimate", "revelacao", 10, "masculina_aguda", "+15%", "+8Hz", 2.0),
    Bordao("daciolo", "daci-05", "Glória a sap... opa, Glória a Deus!", "idle_fail", "confuso", 6, "masculina_aguda", "+0%", "+2Hz", 2.5),
    Bordao("daciolo", "daci-06", "Pela honra e glória de Nosso Senhor!", "spawn", "solene", 8, "masculina_aguda", "+0%", "+3Hz", 2.5),

    # ── XANDAO ──
    Bordao("xandao", "xand-01", "Monocraticamente!", "attack", "autoritario", 9, "masculina_grave", "+0%", "-5Hz", 1.5),
    Bordao("xandao", "xand-02", "Faz silêncio!", "special", "ameacador", 10, "masculina_grave", "+5%", "-3Hz", 1.0),
    Bordao("xandao", "xand-03", "Censurado!", "attack", "imperativo", 9, "masculina_grave", "+10%", "-5Hz", 0.8),
    Bordao("xandao", "xand-04", "Xandaquistão!", "special", "poder_absoluto", 8, "masculina_grave", "-5%", "-5Hz", 1.5),
    Bordao("xandao", "xand-05", "Inquérito das fake news!", "spawn", "ameacador", 7, "masculina_grave", "+0%", "-3Hz", 2.0),

    # ── CIRO ──
    Bordao("ciro", "ciro-01", "Acabou meu Rivotril!", "hit", "desespero", 10, "masculina_aguda", "+20%", "+8Hz", 1.5),
    Bordao("ciro", "ciro-02", "Bossaloide!", "idle", "arrogante", 8, "masculina_aguda", "+10%", "+5Hz", 0.8),
    Bordao("ciro", "ciro-03", "Paçoca", "death", "bug_mental", 4, "masculina_aguda", "-20%", "+0Hz", 0.8),
    Bordao("ciro", "ciro-04", "Eu tenho um plano!", "spawn", "grandioso_vazio", 7, "masculina_aguda", "+5%", "+3Hz", 1.2),
    Bordao("ciro", "ciro-05", "Que brisa, mano", "idle", "chapado", 4, "masculina_aguda", "-15%", "-2Hz", 1.0),
    Bordao("ciro", "ciro-06", "Na próxima eu ganho!", "death", "delusional", 6, "masculina_aguda", "+0%", "+0Hz", 1.2),

    # ── GILMAR ──
    Bordao("gilmar", "gilm-01", "Sou fã, sou fã, sou fã", "idle", "cinico", 6, "masculina_grave", "-5%", "-3Hz", 2.0),
    Bordao("gilmar", "gilm-02", "Vagabundo! Vagabundo! Vagabundo!", "attack", "raiva", 10, "masculina_grave", "+15%", "+3Hz", 2.5),
    Bordao("gilmar", "gilm-03", "Pastel, pastel, pastel!", "special", "prazer", 7, "masculina_grave", "+5%", "+0Hz", 1.5),

    # ── TAXADD ──
    Bordao("taxadd", "taxa-01", "TAXADO!", "attack", "orgulho_compulsivo", 9, "masculina_grave", "+10%", "+3Hz", 0.8),
    Bordao("taxadd", "taxa-02", "Não é imposto, é contribuição!", "idle", "justificativa", 6, "masculina_grave", "+0%", "+0Hz", 2.0),
    Bordao("taxadd", "taxa-03", "Que horas é a merenda?", "idle", "infantil", 5, "masculina_grave", "-10%", "+5Hz", 1.5),

    # ── TRUMP ──
    Bordao("trump", "trump-01", "TREMENDOUS!", "attack", "excitado", 9, "masculina_grave", "+10%", "-5Hz", 1.0),
    Bordao("trump", "trump-02", "FAKE NEWS!", "hit", "indignado", 10, "masculina_grave", "+15%", "-3Hz", 0.8),
    Bordao("trump", "trump-03", "Very good, companheiro!", "idle", "condescendente", 6, "masculina_grave", "+0%", "-5Hz", 1.5),
    Bordao("trump", "trump-04", "This is MY country now. Obrigado.", "special", "imperialista", 7, "masculina_grave", "-5%", "-5Hz", 2.5),

    # ── ENEAS ──
    Bordao("eneas", "eneas-01", "MEU NOME É ENÉAS!", "spawn", "epico", 10, "masculina_grave", "+5%", "-5Hz", 2.0),
    Bordao("eneas", "eneas-02", "MEU NÚMERO É CINQUENTA E SEEEEEIS!", "ultimate", "epico_maximo", 10, "masculina_grave", "+10%", "-5Hz", 3.0),

    # ── EDUARDO ──
    Bordao("eduardo", "edu-01", "Pai! Pai!", "idle", "desesperado", 8, "masculina_aguda", "+10%", "+8Hz", 0.8),
    Bordao("eduardo", "edu-02", "Posso pedir uma embaixada?", "idle", "esperancoso", 5, "masculina_aguda", "+0%", "+5Hz", 1.5),

    # ── JANJA ──
    Bordao("janja", "janja-01", "FORA, ELON MUSK!", "attack", "grito_mundial", 10, "feminina", "+15%", "+5Hz", 1.5),
    Bordao("janja", "janja-02", "Quem manda aqui sou eu, amor.", "idle", "autoritaria", 7, "feminina", "+0%", "+0Hz", 2.0),

    # ── ALCKMIN ──
    Bordao("alckmin", "alck-01", "Eu adoro esse nome, álcool em mim!", "idle", "subserviente", 5, "masculina_grave", "+0%", "+3Hz", 2.0),
    Bordao("alckmin", "alck-02", "Quer que eu passe o café?", "spawn", "servical", 4, "masculina_grave", "-5%", "+2Hz", 1.5),

    # ── MARINA ──
    Bordao("marina", "marina-01", "Eu volto em 4 anos...", "death", "melancolica", 2, "feminina", "-20%", "-3Hz", 2.0),
    Bordao("marina", "marina-02", "Eu estava aqui o tempo todo...", "spawn", "sussurro", 2, "feminina", "-15%", "-2Hz", 2.0),

    # ── MONARK ──
    Bordao("monark", "monark-01", "Mano, pensa comigo...", "game_over", "chapado", 4, "masculina_default", "-15%", "-3Hz", 1.5),
    Bordao("monark", "monark-02", "Bem-vindo ao Limbo.", "game_over", "casual", 5, "masculina_default", "-10%", "-2Hz", 1.2),

    # ── BARROSO ──
    Bordao("barroso", "barr-01", "A sessão está ENCERRADA!", "special", "autoridade_estourada", 10, "masculina_grave", "+10%", "-3Hz", 1.5),
    Bordao("barroso", "barr-02", "Gilmar, pelo amor de Deus, CALA A BOCA!", "attack", "furia_elegante", 9, "masculina_grave", "+15%", "+2Hz", 2.5),

    # ── VORCARO ──
    Bordao("vorcaro", "vorc-01", "Isso não é corrupção, é networking.", "idle", "cinico_frio", 5, "masculina_grave", "-5%", "-2Hz", 2.0),
    Bordao("vorcaro", "vorc-02", "Delação? Vou pensar. Já pensei.", "death", "calculista", 6, "masculina_grave", "+0%", "-3Hz", 2.5),
]


def _get_ssl_context():
    """SSL context que ignora verificacao (para proxy corporativo Netskope)."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


async def generate_single(bordao: Bordao, output_dir: Path) -> dict:
    """Gera MP3 + OGG para um unico bordao."""
    import edge_tts
    import aiohttp

    char_dir = output_dir / bordao.personagem
    char_dir.mkdir(parents=True, exist_ok=True)

    mp3_path = char_dir / f"{bordao.id}.mp3"
    ogg_path = char_dir / f"{bordao.id}.ogg"

    voice = VOICES.get(bordao.voice, VOICES["masculina_default"])

    # Gerar MP3 com edge-tts (SSL patchado no import level)
    communicate = edge_tts.Communicate(
        text=bordao.texto,
        voice=voice,
        rate=bordao.rate,
        pitch=bordao.pitch,
    )
    await communicate.save(str(mp3_path))
    print(f"  [MP3] {bordao.id}: \"{bordao.texto[:40]}...\" -> {mp3_path.name}")

    # Converter para OGG via ffmpeg (melhor para web/Phaser)
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(mp3_path), "-c:a", "libvorbis", "-q:a", "6", str(ogg_path)],
            capture_output=True, check=True,
        )
        print(f"  [OGG] {bordao.id}: -> {ogg_path.name}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"  [WARN] ffmpeg nao encontrado, apenas MP3 gerado para {bordao.id}")

    return {
        "id": bordao.id,
        "personagem": bordao.personagem,
        "texto": bordao.texto,
        "trigger": bordao.trigger,
        "emocao": bordao.emocao,
        "mp3": str(mp3_path.relative_to(BASE_DIR)),
        "ogg": str(ogg_path.relative_to(BASE_DIR)) if ogg_path.exists() else None,
        "voice": voice,
        "rate": bordao.rate,
        "pitch": bordao.pitch,
    }


async def main():
    import argparse

    parser = argparse.ArgumentParser(description="Gera bordoes de audio para Zumbis de Brasilia")
    parser.add_argument("--personagem", "-p", help="Gerar apenas para um personagem (ex: lula, daciolo)")
    parser.add_argument("--list-voices", action="store_true", help="Lista vozes PT-BR disponiveis")
    parser.add_argument("--dry-run", action="store_true", help="Mostra o que seria gerado sem gerar")
    args = parser.parse_args()

    if args.list_voices:
        import edge_tts
        voices = await edge_tts.list_voices()
        pt_voices = [v for v in voices if v["Locale"].startswith("pt-BR")]
        print("\nVozes PT-BR disponiveis:")
        for v in pt_voices:
            print(f"  {v['ShortName']:30s} | {v['Gender']:8s} | {v['FriendlyName']}")
        return

    # Filtrar por personagem se especificado
    bordoes = BORDOES
    if args.personagem:
        bordoes = [b for b in BORDOES if b.personagem == args.personagem]
        if not bordoes:
            nomes = sorted(set(b.personagem for b in BORDOES))
            print(f"Personagem '{args.personagem}' nao encontrado. Disponiveis: {', '.join(nomes)}")
            return

    if args.dry_run:
        print(f"\n[DRY RUN] Geraria {len(bordoes)} bordoes:")
        for b in bordoes:
            print(f"  {b.id:15s} | {b.personagem:12s} | \"{b.texto[:50]}\"")
        return

    print(f"\n🧟 ZUMBIS DE BRASILIA — Gerando {len(bordoes)} bordoes de audio...\n")

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    for bordao in bordoes:
        try:
            entry = await generate_single(bordao, AUDIO_DIR)
            manifest.append(entry)
        except Exception as e:
            print(f"  [ERRO] {bordao.id}: {e}")

    # Salvar manifest JSON (para Phaser 3 carregar)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {len(manifest)} bordoes gerados!")
    print(f"   MP3/OGG em: {AUDIO_DIR}")
    print(f"   Manifest:   {MANIFEST_PATH}")

    # Resumo por personagem
    chars = {}
    for m in manifest:
        chars.setdefault(m["personagem"], []).append(m["id"])
    print("\n📊 Resumo:")
    for char, ids in sorted(chars.items()):
        print(f"   {char:15s}: {len(ids)} bordoes")


if __name__ == "__main__":
    asyncio.run(main())
