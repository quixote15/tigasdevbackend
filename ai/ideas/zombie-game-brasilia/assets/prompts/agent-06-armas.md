Voce e um agente de arte do time "Zumbis de Brasilia". Seu trabalho e criar TODOS os assets de ARMAS E ITENS do jogo.

## Armas do Jogador (Cidadao Comum)
1. **Chinelo Havaianas** — Arma inicial, melee. Chinelo azul de borracha, efeito "THWACK" visual (onomatopeia aparece).
2. **Vassoura da Esplanada** — Melee range. Vassoura de palha velha, cabo de madeira.
3. **Urna Eletronica** — Ranged. Urna velha com fios expostos, dispara votos. Tela quebrada.
4. **Santinho Explosivo** — Projetil. Panfleto eleitoral que explode ao contato.
5. **Crachá Afiado** — Throwing weapon. Cracha de servidor publico afiado como shuriken.
6. **Carimbo de Protocolo** — Melee special. Carimbo gigante de "INDEFERIDO" que stunna.
7. **Microfone do Plenario** — Ranged. Feedback sonoro como ataque.

## Armas Exclusivas dos Bosses
8. **Garrafa de Velho Barreiro Incendiaria** (Lula) — Molotov de cachaca, rotulo visivel, poca de fogo.
9. **Arma que Brocha (as Vezes)** (Bolsonaro) — Revolver dourado com adesivo bandeira BR, 30% falha com fumaca patetica.
10. **Caneta Bicolor** (BolsoLula) — BIC gigante vermelho/verde-amarelo, emendas explosivas.
11. **Martelao da Censura** (Xandao) — Martelo tamanho poste com "CENSURADO" em vermelho, onda de choque.
12. **Toga de Teflon** (Gilmar) — Toga manchada de pastel, bolso com dinheiro caindo.
13. **Biblia Sagrada Blindada** (Daciolo) — Biblia gigante capa titanio, converte inimigos.
14. **Taco de Golfe Nuclear** (Trump) — Taco dourado, bolas com carinha Trump, explosao "TREMENDOUS".
15. **Frasco de Rivotril Turbo** (Ciro) — Frasco gigante como clava, efeito sedacao.
16. **Calculadora Infernal** (Taxadd) — Calculadora gigante, dispara cifras, display "99.99%".
17. **Bigode da Justica** (Eneas) — Bigode boomerang, se destaca do rosto e gira.

## Instrucoes

### Passo 1: Pesquisa Web
- "Andre Guedes zumbis brasilia armas"
- "pixel art weapons satirical game"  
- "Andre Guedes chinelo vassoura"
- "sprite sheet weapon animation 2d game"
- "phaser 3 weapon sprites"

### Passo 2: Leia Documentos
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/research/personagens/top_20_personagens.md` (procure "Arma Exclusiva" em cada personagem)
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/16-frontend-mvp-web-plan.md`
- `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/assets/prompts/context-base.md`

### Passo 3: Gere Assets
Para CADA arma em `assets/armas/[arma]/`:
- `sprites/sprite-spec.md`: Dimensoes (32x32 ou 48x48), cores, detalhes por frame
  - Static/inventory: 1 frame
  - Swing/use: 3-4 frames
  - Projectile flight: 4 frames (se ranged)
  - Impact/explosion: 3 frames
  - Idle glow/effect: 2 frames
- `sprites/art-prompts.md`: Prompts de geracao por sprite
- `animations/animation-spec.md`: Timing de uso, particulas, efeitos visuais (THWACK, fumaca, fogo, cifras)

### Regras Visuais
- Armas devem ser DESPROPORCIONAIS (maiores que o personagem quando possivel)
- Efeitos visuais EXAGERADOS (explosao de cachaca com cogumelo atomico de alcohol)
- Cada arma tem personalidade visual unica
- Projeteis devem ter particulas de trail
- Impactos devem ter screen shake e flash

### Items/Power-ups
Tambem crie specs para power-ups que aparecem no mapa:
- Cafe (heal pequeno) — copinho de cafe de maquina
- Coxinha (heal medio) — coxinha de cantina do Congresso
- Picanha (heal grande) — referencia Lula
- Santinho (score boost) — panfleto eleitoral brilhante
- Crachá VIP (invulnerabilidade temporaria)
- Emenda Pix (score multiplier) — pix verde brilhante

Salve power-ups em `assets/armas/powerups/` (crie a pasta).

Trabalhe em `/Users/ricardo.ribeiro_1/Desktop/my-studies/ai/ideas/zombie-game-brasilia/`.
