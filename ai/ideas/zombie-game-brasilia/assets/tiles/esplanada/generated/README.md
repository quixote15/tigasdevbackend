# Tilesets Gerados — Esplanada dos Ministerios (MVP)

Gerados via PixelLab MCP (`create_topdown_tileset`) em 2026-04-12.
Wang autotile format — 16 tiles cada (4x4 grid, 16x16px por tile).

## Tilesets

| # | Arquivo | Descricao | Tileset ID | Base Tile IDs |
|---|---------|-----------|------------|---------------|
| 01 | concreto-grama | Concreto rachado ↔ Grama seca | `099f9cf9-d3e1-4e20-a296-c513e96105de` | lower: `4d39f97c`, upper: `67e835e1` |
| 02 | concreto-asfalto | Concreto ↔ Asfalto (Eixo Monumental) | `70118b83-3d2a-4e26-97d2-7bbef67fbcdc` | lower: `d47f3cb3`, upper: `5ff83f49` |
| 03 | concreto-agua | Concreto ↔ Agua turva (Espelho D'Agua) | `8a64350f-2ee9-48ef-9792-d938ca058c8b` | lower: `64480b01`, upper: `603cc006` |
| 04 | grama-asfalto | Grama seca ↔ Asfalto | `f8c1ebe7-ae17-4da5-99b5-eb7e0f00c632` | lower: `2deacf48`, upper: `d76a8aef` |

## Uso no Tiled Map Editor

1. Importar cada PNG como tileset (16x16px tile size)
2. Usar Wang tile mode com corner-based autotiling
3. Cada JSON contem `tiles[].corners` com NE/NW/SE/SW = "upper"/"lower"
4. Pintar terrain grid: lower = terreno base, upper = terreno elevado

## Propriedades por terreno

| Terreno | Walkable | Speed Mod | Collision | Kill Zone |
|---------|----------|-----------|-----------|-----------|
| Concreto | sim | 1.0 | nao | nao |
| Grama seca | sim | 0.85 | nao | nao |
| Asfalto | sim | 1.0 | nao | nao |
| Agua turva | NAO | 0 | SIM | SIM |

## Base Tile IDs (para encadear novos tilesets)

Use estes IDs como `lower_base_tile_id` ou `upper_base_tile_id` ao gerar novos tilesets
para garantir consistencia visual entre terrenos conectados:

- Concreto: `4d39f97c-42de-410d-9d6e-dac88ac750d5` ou `5ff83f49-c896-42a4-9093-b515ee69013d`
- Grama: `67e835e1-3a9e-4800-973a-7804203f15cc` ou `d76a8aef-d3a9-42da-82ed-d651ac59d6d7`
- Asfalto: `d47f3cb3-6d1e-437f-8cfb-9b2ac5246506` ou `2deacf48-35b2-4e1d-abce-5d9da7db718b`
- Agua: `64480b01-8721-4629-bdd1-4b608de2a0a8`
