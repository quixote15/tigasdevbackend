# Research — Zumbis de Brasília

Pipeline de extração de personagens a partir dos vídeos de André Guedes.

## Pré-requisitos

```bash
pip3 install yt-dlp anthropic
export ANTHROPIC_API_KEY=sk-ant-...
```

## Pipeline (executar em ordem)

### 1. Baixar vídeos e transcrições

```bash
# Apenas transcrições (rápido, ~50MB)
python3 01_download_videos.py --only-subs

# Com vídeos (~10GB+, demorado)
python3 01_download_videos.py

# Listar sem baixar
python3 01_download_videos.py --list-only

# Limitar quantidade
python3 01_download_videos.py --only-subs --limit 20
```

### 2. Parsear transcrições (limpar VTT/SRT → texto)

```bash
python3 02_parse_transcricoes.py
```

### 3. Extrair personagens com IA

```bash
# Com Sonnet (mais rápido e barato)
python3 03_extrair_personagens.py

# Com Opus (mais detalhado)
python3 03_extrair_personagens.py --model claude-opus-4-20250514
```

## Estrutura de saída

```
research/
├── videos/                    # Vídeos MP4 (720p)
├── transcricoes/              # Legendas VTT/SRT originais + metadados JSON
├── transcricoes_limpas/       # Texto limpo por vídeo + compilado
│   ├── <video_id>.txt
│   ├── _todas_transcricoes.json
│   └── _todas_transcricoes.txt
├── personagens/               # Personagens extraídos
│   ├── _todos_personagens.json    # JSON completo
│   ├── _catalogo_personagens.md   # Catálogo legível
│   └── <nome>.json                # Um arquivo por personagem
└── video_manifest.json        # Lista de todos os vídeos encontrados
```

## O que é extraído por personagem

- **Falas e bordões** — citações diretas das transcrições
- **Perfil** — quem é, o que representa na sátira
- **Personalidade** — trejeitos, forma de falar, comportamento
- **Skin (aparência)** — traços físicos, roupas, acessórios, deformações no estilo André Guedes
- **Skills para o jogo** — 2-3 habilidades satirizando a atuação política real
- **Potencial para o jogo** — nota 1-5 e papel sugerido (boss, inimigo, NPC, jogável)
