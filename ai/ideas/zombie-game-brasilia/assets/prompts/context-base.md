# Contexto Base — Zumbis de Brasilia Asset Pipeline

## Estilo Visual Andre Guedes
- Caricaturas GROTESCAS, underground comix, deformadas
- Paleta: cores saturadas-sujas, ceu laranja-sangue, gas verde doentio
- Animacao: twitchy, jerky, deformacao organica (NAO suave)
- Cada personagem tem uma DEFORMIDADE ANATOMICA que E a piada
- Tracos: linhas grossas, sombras pesadas, exagero proposital
- Inspiracao: Robert Crumb + humor politico brasileiro + horror B-movie

## Specs Tecnicas (Phaser 3)
- Sprite atlas unico: 2048x2048px
- Sprites individuais: 64x64px (personagens), 32x32px (projeteis), 16x16px (tiles)
- Formatos: PNG com transparencia
- Animacoes: sprite sheets horizontais
  - Idle: 4 frames
  - Walk: 6 frames  
  - Attack: 3 frames
  - Death: 4 frames
  - Hit: 2 frames
  - Special: 4-8 frames (varia por personagem)
- Frame rate: 8-12 fps para animacao (estilo jerky do Andre Guedes)
- Perspectiva: top-down levemente isometrica (Y-sorting)

## Output Esperado por Personagem
1. `sprite-spec.md` — Especificacao detalhada de cada sprite/frame
2. `art-prompts.md` — Prompts para geracao de imagem (Stable Diffusion / DALL-E / Midjourney)
3. `animation-spec.md` — Ciclos de animacao, timing, efeitos
4. `skin-variants.md` — Variantes de skin (normal, 2026, zombie, etc.)
5. `reference-urls.md` — URLs de referencia encontradas na web
6. `audio-script.md` — Bordoes com timing e instrucoes TTS

## Diretorio Base
`/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/assets/`
