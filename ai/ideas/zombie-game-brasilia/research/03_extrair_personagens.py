#!/usr/bin/env python3
"""
Extrai personagens das transcrições do André Guedes usando Claude API.
Para cada personagem encontrado, extrai: falas, perfil, características,
skin (aparência visual) e armas/skills.

Uso:
    python3 03_extrair_personagens.py [--model claude-sonnet-4-20250514]

Requer:
    ANTHROPIC_API_KEY no ambiente ou em .env
"""

import json
import os
import sys
import argparse
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("❌ Instale: pip3 install anthropic")
    sys.exit(1)

BASE_DIR = Path(__file__).parent
TRANSCRICOES_CLEAN_DIR = BASE_DIR / "transcricoes_limpas"
PERSONAGENS_DIR = BASE_DIR / "personagens"

EXTRACTION_PROMPT = """Você é um especialista na obra do cartunista André Guedes, criador de "Zumbis de Brasília" e "Limbo dos Cancelados".

Analise as transcrições abaixo dos vídeos de sátira política do André Guedes e extraia TODOS os personagens que aparecem.

Para CADA personagem, extraia:

1. **Nome/Apelido**: Como é chamado no vídeo (pode ser nome real de político ou apelido satírico)
2. **Tipo**: Político real satirizado | Arquétipo genérico | Personagem fictício | Narrador/Apresentador
3. **Falas**: Todas as falas e bordões do personagem (citações diretas das transcrições)
4. **Perfil**: Quem é essa figura, o que representa, qual seu papel na sátira
5. **Características de Personalidade**: Trejeitos, manias, forma de falar, comportamento
6. **Aparência Visual (Skin)**: Como André Guedes o desenha — traços físicos exagerados, roupas, acessórios, cores, deformações grotescas. Se não for descrito explicitamente, INFIRA baseado no estilo de caricatura do André Guedes.
7. **Armas/Skills para o Jogo**: Baseado na personalidade e falas, sugira 2-3 habilidades/armas que esse personagem teria num jogo de zumbi. Cada skill deve ser uma sátira da atuação política real.
8. **Aparições**: Em quais vídeos esse personagem aparece (liste os títulos)
9. **Potencial para o Jogo**: Nota 1-5 de quão bom seria como personagem jogável ou inimigo

Responda EXCLUSIVAMENTE em JSON válido com esta estrutura:
```json
{
  "personagens": [
    {
      "nome": "string",
      "tipo": "político_real | arquétipo | fictício | narrador",
      "inspirado_em": "nome real se for político, null se não",
      "falas": ["fala 1", "fala 2"],
      "bordoes": ["bordão 1"],
      "perfil": "string com descrição do papel na sátira",
      "personalidade": {
        "trejeitos": ["trejeito 1"],
        "forma_de_falar": "string",
        "comportamento": "string"
      },
      "skin": {
        "tracos_fisicos": "string descrevendo aparência caricata",
        "roupas": "string",
        "acessorios": ["acessório 1"],
        "cores_dominantes": ["cor 1"],
        "deformacoes_grotescas": "string no estilo André Guedes"
      },
      "skills_jogo": [
        {
          "nome": "string nome da skill",
          "descricao": "string o que faz no jogo",
          "referencia_politica": "string qual ação política real satiriza"
        }
      ],
      "aparicoes": ["título do vídeo 1"],
      "potencial_jogo": {
        "nota": 5,
        "papel_sugerido": "jogável | boss | inimigo_comum | npc_aliado | npc_neutro",
        "justificativa": "string"
      }
    }
  ],
  "resumo": {
    "total_personagens": 0,
    "politicos_reais": 0,
    "arquetipos": 0,
    "ficticios": 0,
    "top_5_para_jogo": ["nome 1", "nome 2"]
  }
}
```

IMPORTANTE:
- Extraia TODOS os personagens, mesmo os que aparecem brevemente
- Para políticos reais, descreva a CARICATURA, não a pessoa real
- As skills devem ser humorísticas e satirizar a atuação política
- A aparência visual deve seguir o estilo grotesco de André Guedes
- Se um personagem aparece em vários vídeos, consolide as informações"""


def load_transcriptions() -> dict:
    """Carrega transcrições limpas."""
    compiled = TRANSCRICOES_CLEAN_DIR / "_todas_transcricoes.json"
    if compiled.exists():
        return json.loads(compiled.read_text())

    # Fallback: carregar arquivos individuais
    transcriptions = {}
    for txt_file in sorted(TRANSCRICOES_CLEAN_DIR.glob("*.txt")):
        if txt_file.name.startswith("_"):
            continue
        content = txt_file.read_text()
        lines = content.split("\n")
        title = lines[0].replace("# ", "") if lines else txt_file.stem
        text = "\n".join(lines[2:]) if len(lines) > 2 else content
        transcriptions[txt_file.stem] = {
            "title": title,
            "text": text,
            "word_count": len(text.split()),
        }
    return transcriptions


def chunk_transcriptions(transcriptions: dict, max_chars: int = 150_000) -> list[str]:
    """Divide transcrições em chunks que cabem no context do Claude."""
    chunks = []
    current = ""

    for vid_id, data in transcriptions.items():
        entry = f"\n--- VÍDEO: {data['title']} ---\n{data['text']}\n"
        if len(current) + len(entry) > max_chars:
            if current:
                chunks.append(current)
            current = entry
        else:
            current += entry

    if current:
        chunks.append(current)

    return chunks


def extract_characters(client: anthropic.Anthropic, chunk: str, chunk_num: int, total: int, model: str) -> dict:
    """Usa Claude para extrair personagens de um chunk de transcrições."""
    print(f"\n🤖 Analisando chunk {chunk_num}/{total} ({len(chunk):,} chars)...")

    message = client.messages.create(
        model=model,
        max_tokens=16000,
        messages=[
            {
                "role": "user",
                "content": f"{EXTRACTION_PROMPT}\n\n## TRANSCRIÇÕES PARA ANÁLISE:\n\n{chunk}",
            }
        ],
    )

    response_text = message.content[0].text

    # Extrair JSON da resposta
    try:
        # Tentar parsear direto
        return json.loads(response_text)
    except json.JSONDecodeError:
        # Tentar extrair JSON de dentro de markdown code block
        import re
        json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        # Última tentativa: encontrar o primeiro { até o último }
        start = response_text.find("{")
        end = response_text.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response_text[start:end])
        raise ValueError(f"Não foi possível extrair JSON da resposta:\n{response_text[:500]}")


def merge_characters(all_results: list[dict]) -> dict:
    """Merge personagens de múltiplos chunks, consolidando duplicatas."""
    merged = {}

    for result in all_results:
        for char in result.get("personagens", []):
            name = char["nome"].lower().strip()
            if name in merged:
                # Merge falas, aparições, etc.
                existing = merged[name]
                existing["falas"] = list(set(existing.get("falas", []) + char.get("falas", [])))
                existing["bordoes"] = list(set(existing.get("bordoes", []) + char.get("bordoes", [])))
                existing["aparicoes"] = list(set(existing.get("aparicoes", []) + char.get("aparicoes", [])))
                # Manter skills se tiver mais
                if len(char.get("skills_jogo", [])) > len(existing.get("skills_jogo", [])):
                    existing["skills_jogo"] = char["skills_jogo"]
                # Manter maior nota
                if char.get("potencial_jogo", {}).get("nota", 0) > existing.get("potencial_jogo", {}).get("nota", 0):
                    existing["potencial_jogo"] = char["potencial_jogo"]
            else:
                merged[name] = char

    # Ordenar por potencial de jogo
    sorted_chars = sorted(merged.values(),
                          key=lambda c: c.get("potencial_jogo", {}).get("nota", 0),
                          reverse=True)

    # Calcular resumo
    politicos = sum(1 for c in sorted_chars if c.get("tipo") == "político_real")
    arquetipos = sum(1 for c in sorted_chars if c.get("tipo") == "arquétipo")
    ficticios = sum(1 for c in sorted_chars if c.get("tipo") in ("fictício", "narrador"))
    top5 = [c["nome"] for c in sorted_chars[:5]]

    return {
        "personagens": sorted_chars,
        "resumo": {
            "total_personagens": len(sorted_chars),
            "politicos_reais": politicos,
            "arquetipos": arquetipos,
            "ficticios": ficticios,
            "top_5_para_jogo": top5,
        }
    }


def save_individual_files(data: dict):
    """Salva um arquivo por personagem para referência rápida."""
    for char in data["personagens"]:
        name_safe = char["nome"].lower().replace(" ", "_").replace("/", "_")
        name_safe = "".join(c for c in name_safe if c.isalnum() or c == "_")
        filepath = PERSONAGENS_DIR / f"{name_safe}.json"
        filepath.write_text(json.dumps(char, ensure_ascii=False, indent=2))

    # Salvar resumo em markdown legível
    md_lines = ["# Personagens — Zumbis de Brasília (André Guedes)\n"]
    md_lines.append(f"**Total**: {data['resumo']['total_personagens']} personagens\n")
    md_lines.append(f"**Top 5 para o jogo**: {', '.join(data['resumo']['top_5_para_jogo'])}\n")

    for char in data["personagens"]:
        md_lines.append(f"\n---\n\n## {char['nome']}")
        md_lines.append(f"**Tipo**: {char.get('tipo', '?')} | "
                        f"**Inspirado em**: {char.get('inspirado_em', '?')} | "
                        f"**Potencial**: {char.get('potencial_jogo', {}).get('nota', '?')}/5 "
                        f"({char.get('potencial_jogo', {}).get('papel_sugerido', '?')})")
        md_lines.append(f"\n**Perfil**: {char.get('perfil', '?')}")

        skin = char.get("skin", {})
        md_lines.append(f"\n### Aparência (Skin)")
        md_lines.append(f"- **Traços**: {skin.get('tracos_fisicos', '?')}")
        md_lines.append(f"- **Roupas**: {skin.get('roupas', '?')}")
        md_lines.append(f"- **Acessórios**: {', '.join(skin.get('acessorios', []))}")
        md_lines.append(f"- **Cores**: {', '.join(skin.get('cores_dominantes', []))}")
        md_lines.append(f"- **Deformações**: {skin.get('deformacoes_grotescas', '?')}")

        md_lines.append(f"\n### Skills para o Jogo")
        for skill in char.get("skills_jogo", []):
            md_lines.append(f"- **{skill.get('nome', '?')}**: {skill.get('descricao', '?')} "
                            f"_(ref: {skill.get('referencia_politica', '?')})_")

        if char.get("bordoes"):
            md_lines.append(f"\n### Bordões")
            for b in char["bordoes"]:
                md_lines.append(f'- "{b}"')

        if char.get("falas"):
            md_lines.append(f"\n### Falas ({len(char['falas'])} encontradas)")
            for f in char["falas"][:10]:  # Máx 10 por personagem no MD
                md_lines.append(f'- "{f}"')
            if len(char["falas"]) > 10:
                md_lines.append(f"- _...e mais {len(char['falas']) - 10} falas_")

    md_file = PERSONAGENS_DIR / "_catalogo_personagens.md"
    md_file.write_text("\n".join(md_lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Extrair personagens das transcrições")
    parser.add_argument("--model", type=str, default="claude-sonnet-4-20250514",
                        help="Modelo Claude a usar (default: claude-sonnet-4-20250514)")
    args = parser.parse_args()

    # Verificar API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        env_file = Path.home() / ".env"
        if env_file.exists():
            for line in env_file.read_text().split("\n"):
                if line.startswith("ANTHROPIC_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"')
        # Tentar .env local
        local_env = BASE_DIR.parent / ".env"
        if not api_key and local_env.exists():
            for line in local_env.read_text().split("\n"):
                if line.startswith("ANTHROPIC_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"')

    if not api_key:
        print("❌ ANTHROPIC_API_KEY não encontrada.")
        print("   Defina via: export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    PERSONAGENS_DIR.mkdir(parents=True, exist_ok=True)

    # Carregar transcrições
    transcriptions = load_transcriptions()
    if not transcriptions:
        print("❌ Nenhuma transcrição encontrada.")
        print("   Execute primeiro:")
        print("   1. python3 01_download_videos.py --only-subs")
        print("   2. python3 02_parse_transcricoes.py")
        sys.exit(1)

    print(f"📚 Carregadas {len(transcriptions)} transcrições")
    total_words = sum(d["word_count"] for d in transcriptions.values())
    print(f"   {total_words:,} palavras totais")

    # Dividir em chunks
    chunks = chunk_transcriptions(transcriptions)
    print(f"   Dividido em {len(chunks)} chunks para análise")

    # Extrair personagens com Claude
    client = anthropic.Anthropic(api_key=api_key)
    all_results = []

    for i, chunk in enumerate(chunks, 1):
        try:
            result = extract_characters(client, chunk, i, len(chunks), args.model)
            chars_found = len(result.get("personagens", []))
            print(f"   ✅ {chars_found} personagens encontrados no chunk {i}")
            all_results.append(result)
        except Exception as e:
            print(f"   ❌ Erro no chunk {i}: {e}")
            continue

    if not all_results:
        print("❌ Nenhum resultado obtido.")
        sys.exit(1)

    # Merge e consolidar
    print("\n🔄 Consolidando personagens...")
    final = merge_characters(all_results)

    # Salvar resultado completo
    output_json = PERSONAGENS_DIR / "_todos_personagens.json"
    output_json.write_text(json.dumps(final, ensure_ascii=False, indent=2))

    # Salvar arquivos individuais + catálogo MD
    save_individual_files(final)

    print(f"\n{'='*60}")
    print(f"✅ EXTRAÇÃO COMPLETA!")
    print(f"{'='*60}")
    print(f"   Total personagens: {final['resumo']['total_personagens']}")
    print(f"   Políticos reais: {final['resumo']['politicos_reais']}")
    print(f"   Arquétipos: {final['resumo']['arquetipos']}")
    print(f"   Fictícios: {final['resumo']['ficticios']}")
    print(f"   Top 5 para jogo: {', '.join(final['resumo']['top_5_para_jogo'])}")
    print(f"\n📁 Resultados em: {PERSONAGENS_DIR}")
    print(f"   _todos_personagens.json  — JSON completo")
    print(f"   _catalogo_personagens.md — Catálogo legível")
    print(f"   <nome>.json              — Um arquivo por personagem")


if __name__ == "__main__":
    main()
