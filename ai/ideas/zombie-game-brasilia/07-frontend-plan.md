# ZUMBIS DE BRASÍLIA — Plano de Implementação Frontend
### Cada Frame Importa. Cada Toque Importa. Cada Pixel Importa.

**Versão 1.0 | Abril 2026**
**Masahiro Sakurai — Game Feel & Frontend Architecture**

---

> *"A diferença entre um jogo bom e um jogo memorável está nos 16 milissegundos que ninguém vê. É no frame que o jogador não percebe conscientemente, mas sente no intestino. Game feel não é feature — é o jogo em si."*

---

## 1. Rendering Pipeline

### Visão Geral da Pipeline

O Samsung Galaxy A06 tem o Helio G85 — um chip decente mas não generoso. Cada draw call tem peso real. A filosofia é: **renderizar menos, renderizar melhor**.

```
[Canvas Items — Node2D tree]
          ↓
[Godot Compatibility Renderer (OpenGL ES 3.0)]
          ↓
[CanvasGroup batching — sprites por material/textura]
          ↓
[2 Shader passes por frame: world + HUD]
          ↓
[Framebuffer 720×1600 (A06) ou sub-resolução dinâmica]
          ↓
[Display output via Android Surface]
```

### Layers e Z-Ordering

Separação clara de layers é essencial para batching e para o visual estilo HQ funcionar:

| Layer Z | Conteúdo | Tipo de Node | Notas |
|---|---|---|---|
| -10 a -1 | Parallax de fundo (céu, Congresso, árvores) | ParallaxBackground | Sem shader, textura única |
| 0 | TileMap — chão da Esplanada | TileMapLayer | 1 tileset atlas, máx 64 tiles únicos |
| 1 | Sombras projetadas (sprites simples escuros, alpha 40%) | Sprite2D | Renderizados antes dos personagens |
| 2-10 | Entidades dinâmicas (zumbis, pickups) | CharacterBody2D | Z calculado por `position.y / 10` |
| 11 | Player | CharacterBody2D | Sempre acima dos zumbis |
| 12 | Projéteis e power-ups | Area2D | |
| 13-20 | VFX — partículas de impacto, sangue, papéis | CPUParticles2D / GPUParticles2D | Blend por cima das entidades |
| 21 | Onomatopeias de impacto (THWACK, SLAP) | Node2D temporário | Lifetime de 6 frames |
| 100+ | HUD (CanvasLayer) | CanvasLayer | Fora do world space |

**Y-Sort automático:** O nó `Entities` tem `y_sort_enabled = true`. Zumbi mais abaixo na tela aparece na frente — simula profundidade sem câmera 3D.

```gdscript
# Em zombie_base.gd — z_index dinâmico baseado em Y
func _process(_delta: float) -> void:
    z_index = int(global_position.y / 10.0)
```

### Camera System

Câmera em `gameplay.tscn` é um `Camera2D` com comportamento suave:

```gdscript
# src/entities/player/player_camera.gd
class_name PlayerCamera extends Camera2D

@export var follow_speed: float = 8.0       # lerp factor
@export var lead_distance: float = 40.0     # câmera lidera levemente na direção do movimento
@export var bounds_margin: float = 64.0     # câmera para antes da borda do mapa

var _shake_trauma: float = 0.0
var _shake_time: float = 0.0
const SHAKE_DECAY: float = 4.0
const MAX_SHAKE_OFFSET: float = 12.0

func _physics_process(delta: float) -> void:
    # Follow com lead
    var target_pos := owner.global_position
    if owner.velocity.length() > 10.0:
        target_pos += owner.velocity.normalized() * lead_distance
    global_position = global_position.lerp(target_pos, follow_speed * delta)

    # Screen shake
    if _shake_trauma > 0.0:
        _shake_trauma = max(0.0, _shake_trauma - SHAKE_DECAY * delta)
        var shake_amount := _shake_trauma * _shake_trauma  # quadrático = mais natural
        offset = Vector2(
            randf_range(-MAX_SHAKE_OFFSET, MAX_SHAKE_OFFSET) * shake_amount,
            randf_range(-MAX_SHAKE_OFFSET, MAX_SHAKE_OFFSET) * shake_amount
        )
    else:
        offset = Vector2.ZERO

func add_trauma(amount: float) -> void:
    _shake_trauma = min(1.0, _shake_trauma + amount)
```

**Limites do mapa:** `LimitLeft`, `LimitRight`, `LimitTop`, `LimitBottom` definidos no inspector para o tamanho do mapa Esplanada (estimado 2048×1536px). Camera não mostra área além do mapa.

---

## 2. Animation System

### Decisão: Sprite Sheets com AnimatedSprite2D (sem Spine/DragonBones)

**Justificativa técnica:**
- Spine/DragonBones adicionam complexidade de runtime e dependência de plugin
- O estilo André Guedes é *deliberadamente* de frames discretos — não interpolação suave
- Sprite sheets são 100% compatíveis com OpenGL ES 3.0 sem shader extra
- No A06 com 4GB RAM, um atlas de 2048×2048 cabe folgado

**A regra de 12fps para personagens** (citada no UX doc) é proposital. Animação de 12fps com frames expressivos tem mais personalidade que 60fps suave. A expressividade compensa a fluidez.

### Estrutura de AnimatedSprite2D por Entidade

Cada entidade tem **um único** `AnimatedSprite2D` com múltiplas animações nomeadas:

```
AnimatedSprite2D (player)
├── SpriteFrames resource → player_atlas.png (2048×512)
├── Animations:
│   ├── "idle"         → 2 frames, 6fps, loop true
│   ├── "run"          → 4 frames, 12fps, loop true
│   ├── "attack_start" → 2 frames, 24fps, loop false  ← wind-up rápido
│   ├── "attack_hit"   → 1 frame, 24fps, loop false   ← frame de impacto
│   ├── "hurt"         → 2 frames, 12fps, loop false
│   └── "death"        → 8 frames, 12fps, loop false
```

**Blending entre animações:**

Godot 4 não tem blend tree nativo para 2D. Implementar via código com prioridade:

```gdscript
# src/entities/player/player_animator.gd
class_name PlayerAnimator extends Node

enum AnimPriority { IDLE = 0, MOVE = 1, ATTACK = 2, HURT = 3, DEATH = 4 }

var _current_priority: int = AnimPriority.IDLE
@onready var _sprite: AnimatedSprite2D = $"../AnimatedSprite2D"

func play(anim_name: String, priority: int, force: bool = false) -> void:
    if priority >= _current_priority or force:
        _current_priority = priority
        _sprite.play(anim_name)

func _on_animation_finished() -> void:
    # Prioridade cai ao terminar animação one-shot
    if _current_priority in [AnimPriority.ATTACK, AnimPriority.HURT]:
        _current_priority = AnimPriority.IDLE
```

### Frame Rates por Tipo de Animação

| Tipo | FPS | Lógica |
|---|---|---|
| Personagem idle/run | 12fps | Estilo HQ, expressivo |
| Ataque wind-up | 24fps | Precisa ser rápido — responsividade |
| Hit stop (congelamento) | Pausa no frame | Engine.time_scale = 0.05 por 3 frames |
| Morte de zumbi | 12fps | Dramático, não apressado |
| Morte do Boss | 8fps | Cada frame conta — peso máximo |
| VFX de impacto (onomatopeia) | 24fps | Aparece e some rápido |
| Partículas | 30fps máx (A06) | GPUParticles2D com budget |
| UI transitions | 60fps | Smooth, sem choppiness |

### Flip Horizontal para Direção

Sem precisar de animações espelhadas no atlas:

```gdscript
# Em zombie_base.gd
func _face_target(target_pos: Vector2) -> void:
    $AnimatedSprite2D.flip_h = target_pos.x < global_position.x
```

---

## 3. Touch Input System

### Filosofia: Input que Desaparece

O melhor controle touch é o que o jogador esquece que está usando. O joystick virtual dinâmico serve a isso — aparece onde o dedo está, não onde o jogador precisa colocar o dedo.

### Joystick Virtual Dinâmico

```gdscript
# src/ui/virtual_joystick.gd
class_name VirtualJoystick extends Node2D

@export var dead_zone_radius: float = 8.0      # pixels — movimento mínimo para registrar
@export var max_radius: float = 60.0            # raio máximo do joystick (dp → pixels)
@export var follow_speed: float = 10.0          # velocidade de snap do ponto central

var active_touch_index: int = -1
var origin: Vector2 = Vector2.ZERO
var direction: Vector2 = Vector2.ZERO           # vetor normalizado para player_controller

@onready var outer_ring: Sprite2D = $OuterRing  # 120×120px, 40% alpha
@onready var inner_dot: Sprite2D = $InnerDot    # 40×40px, 100% alpha

func _input(event: InputEvent) -> void:
    if event is InputEventScreenTouch:
        _handle_touch(event)
    elif event is InputEventScreenDrag:
        _handle_drag(event)

func _handle_touch(event: InputEventScreenTouch) -> void:
    # Metade esquerda da tela = joystick zone
    if event.position.x > get_viewport().size.x * 0.5:
        return

    if event.pressed and active_touch_index == -1:
        active_touch_index = event.index
        origin = event.position
        global_position = origin
        visible = true
        # Fade in suave (não pop — naturalidade)
        modulate.a = 0.0
        var tween := create_tween()
        tween.tween_property(self, "modulate:a", 1.0, 0.08)
    elif not event.pressed and event.index == active_touch_index:
        _release()

func _handle_drag(event: InputEventScreenDrag) -> void:
    if event.index != active_touch_index:
        return
    var delta := event.position - origin
    var dist := delta.length()
    if dist < dead_zone_radius:
        direction = Vector2.ZERO
        inner_dot.position = Vector2.ZERO
        return
    direction = delta.normalized()
    inner_dot.position = direction * min(dist, max_radius)

func _release() -> void:
    active_touch_index = -1
    direction = Vector2.ZERO
    var tween := create_tween()
    tween.tween_property(self, "modulate:a", 0.0, 0.1)
    await tween.finished
    visible = false
```

### Auto-Aim Suave

Auto-aim de 30 graus (padrão) faz o jogador se sentir mais habilidoso sem sentir que o jogo está jogando por ele. Implementado no `player_controller.gd`:

```gdscript
# src/entities/player/player_controller.gd
const AUTO_AIM_ANGLE: float = deg_to_rad(30.0)  # configurável via settings
const AUTO_AIM_RANGE: float = 200.0

func _get_aim_direction() -> Vector2:
    var base_dir := joystick.direction
    if base_dir.length() < 0.1:
        return _last_aim_dir  # mantém última direção ao parar

    # Busca zumbi mais próximo dentro do cone de auto-aim
    var best_zombie: Node2D = null
    var best_angle: float = AUTO_AIM_ANGLE + 0.01  # maior que threshold = sem assist

    for zombie in get_tree().get_nodes_in_group("zombies"):
        if not zombie.is_alive():
            continue
        var to_zombie := (zombie.global_position - global_position)
        if to_zombie.length() > AUTO_AIM_RANGE:
            continue
        var angle := base_dir.angle_to(to_zombie.normalized())
        if abs(angle) < best_angle:
            best_angle = abs(angle)
            best_zombie = zombie

    if best_zombie != null:
        # Interpola suavemente entre direção do joystick e direção do zumbi
        var to_target := (best_zombie.global_position - global_position).normalized()
        return base_dir.slerp(to_target, 0.6)  # 60% assist, 40% player direction

    return base_dir
```

### Botão de Ataque e Input Buffering

Input buffering de 6 frames (100ms a 60fps) — o toque registra mesmo que chegue alguns frames antes do cooldown terminar:

```gdscript
# src/entities/player/player_controller.gd
const INPUT_BUFFER_FRAMES: int = 6

var _attack_buffer: int = 0

func _input(event: InputEvent) -> void:
    if event is InputEventScreenTouch and event.pressed:
        if event.position.x > get_viewport().size.x * 0.5:
            _attack_buffer = INPUT_BUFFER_FRAMES

func _physics_process(_delta: float) -> void:
    if _attack_buffer > 0:
        _attack_buffer -= 1
        if _can_attack():
            _execute_attack()
            _attack_buffer = 0
```

**Dead zones:**
- Joystick: 8px raio mínimo (evita tremor de mão)
- Botão de ataque: 72dp, registra qualquer toque na metade direita inferior (não só no círculo visível)
- Zona de pausa: 40dp no canto superior — longe do botão de ataque para evitar acidente

### Gesture Recognition

Somente 2 gestures necessárias além do joystick:

| Gesture | Ação | Detecção |
|---|---|---|
| Swipe rápido (>200px/s) na metade direita | Ativar power-up | `InputEventScreenDrag.velocity.length() > 800` |
| Long press no slot de power-up | Ativar power-up | Timer de 0.4s no nó do slot |

---

## 4. Combat Feel

### A Anatomia de um Kill em Código

O hit stop é a peça mais crítica do game feel. 3 frames de pausa (a 60fps = 50ms) é imperceptível como tempo mas registra como peso físico:

```gdscript
# src/systems/combat_system.gd

func process_hit(target: ZombieBase, weapon: WeaponData, hit_pos: Vector2) -> void:
    var damage := _calculate_damage(weapon)
    var is_crit := randf() < GameState.crit_chance

    # 1. HIT STOP — pausa de Engine (afeta apenas physics, não input)
    _apply_hit_stop(3 if not is_crit else 4)

    # 2. HIT FLASH — sprite branco por 2 frames
    target.flash_white(2)

    # 3. SFX imediato (não aguarda hit stop terminar)
    AudioManager.play_sfx_at(weapon.sfx_hit, hit_pos, 0.9 + randf() * 0.2)

    # 4. Knockback no zumbi
    var knockback_dir := (target.global_position - hit_pos).normalized()
    target.apply_knockback(knockback_dir * weapon.knockback_force)

    # 5. Damage number popup
    _spawn_damage_number(hit_pos, damage, is_crit)

    # 6. Onomatopeia visual
    _spawn_onomatopeia(hit_pos, weapon.weapon_id)

    # 7. Screen shake (via câmera)
    Camera.add_trauma(0.15 if not is_crit else 0.25)

    # 8. Haptic
    Input.vibrate_handheld(15 if not is_crit else 30)

    # Aplica dano após toda a apresentação visual
    target.take_damage(damage)

func _apply_hit_stop(frames: int) -> void:
    Engine.time_scale = 0.05  # quase parado
    # Timer em tempo real (ignora time_scale)
    await get_tree().create_timer(frames / 60.0, true).timeout
    Engine.time_scale = 1.0
```

**Flash branco no sprite do zumbi:**

```gdscript
# Em zombie_base.gd
func flash_white(frames: int) -> void:
    $AnimatedSprite2D.material = preload("res://assets/materials/hit_flash.tres")
    await get_tree().create_timer(frames / 60.0).timeout
    $AnimatedSprite2D.material = null
```

O material `hit_flash.tres` é um `ShaderMaterial` com o shader mais simples possível (ver seção 10).

### Screen Shake — Parâmetros Completos

| Evento | Trauma adicionado | Resultado em pixels (max) |
|---|---|---|
| Hit normal (vassoura, chinelo) | 0.15 | ~0.27px² × 12 = ~3.2px |
| Hit crítico | 0.25 | ~0.75px |
| Boss hit | 0.35 | ~1.47px |
| Levar dano | 0.20 | ~0.48px |
| Boss kill | 0.70 | ~5.88px + duração longa |
| Explosão de urna | 0.80 | ~7.68px |
| Kill em combo x10+ | 0.10 | ~0.12px — muito sutil |

*Nota: trauma decai quadrático (trauma²), então valores grandes decaem rápido. 0.7 de trauma resulta em shake perceptível mas que some em ~0.2s.*

### Hitstop Variável por Situação

| Situação | Frames de hitstop | Notas |
|---|---|---|
| Hit normal | 3 frames (~50ms) | Peso básico |
| Hit crítico | 4 frames (~67ms) | Mais peso |
| Boss hit | 5 frames (~83ms) | Impacto de chefe |
| Boss kill (fase final) | 18 frames (~300ms) | Pausa dramática prolongada |
| Multi-hit (urna, área) | 2 frames por hit, max 8 acumulados | Evita travamento longo |

### Damage Numbers

```gdscript
# src/ui/damage_number.gd
class_name DamageNumber extends Node2D

@onready var label: Label = $Label

func setup(value: int, is_crit: bool) -> void:
    label.text = str(value)

    if is_crit:
        label.add_theme_font_size_override("font_size", 28)
        label.modulate = Color("#FFD700")  # dourado
        # Estrela de crítico ao lado
        $CritStar.visible = true
    else:
        label.add_theme_font_size_override("font_size", 20)
        label.modulate = Color.WHITE

    # Animação: sobe com bounce, some
    var tween := create_tween()
    tween.tween_property(self, "position:y", position.y - 40.0, 0.6).set_ease(Tween.EASE_OUT)
    tween.parallel().tween_property(self, "modulate:a", 0.0, 0.6).set_delay(0.3)
    tween.tween_callback(func(): PoolManager.release_damage_number(self))
```

---

## 5. UI Implementation

### HUD — Implementação por Componente

**Estrutura no CanvasLayer:**

```
HUD (CanvasLayer — layer 10)
├── TopBar (HBoxContainer — anchor: top stretch)
│   ├── VidaContainer (HBoxContainer)
│   │   └── HeartIcon × 5 (TextureRect, 32×32px cada)
│   ├── WaveLabel (Label — Bebas Neue 22sp, centro)
│   │   └── ZombiesRestantes (Label — 14sp, abaixo do wave)
│   └── ScoreContainer (VBoxContainer — direita)
│       ├── ScoreLabel (Label — Bebas Neue 28sp, amarelo-ouro)
│       └── ComboLabel (Label — 18sp, laranja, hidden por padrão)
├── BottomBar (Control — anchor: bottom stretch)
│   ├── JoystickArea (Control — metade esquerda, transparente)
│   ├── PowerUpSlot (TextureRect 60×60dp — centro, hidden por padrão)
│   └── AttackButton (TextureButton — direita, 72×72dp)
│       └── CooldownArc (Arc2D ou custom Control)
└── PauseButton (TextureButton — top-right, 40×40dp)
```

**Corações de Vida — Animação de Perda:**

```gdscript
# src/ui/hud.gd
func _on_player_damaged(_amount: float, _source: Node) -> void:
    var hearts := $TopBar/VidaContainer.get_children()
    var current_hp := GameState.current_hp
    var heart_to_break := hearts[current_hp]  # o próximo coração intacto

    # Animação de "quebrar": escala e volta, com flash vermelho na tela
    var tween := create_tween()
    tween.tween_property(heart_to_break, "scale", Vector2(1.4, 1.4), 0.05)
    tween.tween_property(heart_to_break, "scale", Vector2(0.0, 0.0), 0.1)
    tween.tween_callback(func(): heart_to_break.texture = preload("res://assets/ui/heart_empty.png"))
    tween.tween_property(heart_to_break, "scale", Vector2(1.0, 1.0), 0.05)

    # Screen flash vermelho
    $DamageFlash.visible = true
    $DamageFlash.modulate.a = 0.35
    var flash_tween := create_tween()
    flash_tween.tween_property($DamageFlash, "modulate:a", 0.0, 0.15)
    flash_tween.tween_callback(func(): $DamageFlash.visible = false)
```

**Score — Animação de Bounce:**

```gdscript
func _on_score_changed(new_score: int) -> void:
    $TopBar/ScoreContainer/ScoreLabel.text = str(new_score)
    # Bounce: escala 1.3 e volta em 0.15s
    var tween := create_tween()
    tween.tween_property($TopBar/ScoreContainer/ScoreLabel, "scale", Vector2(1.3, 1.3), 0.06)
    tween.tween_property($TopBar/ScoreContainer/ScoreLabel, "scale", Vector2(1.0, 1.0), 0.09)\
        .set_ease(Tween.EASE_OUT).set_trans(Tween.TRANS_ELASTIC)
```

### Transições de Tela

Usando `SceneManager` (autoload) com 3 tipos de transição:

```gdscript
# src/autoloads/scene_manager.gd

enum TransitionType { FADE_BLACK, SLASH_HORIZONTAL, INSTANT }

func change_scene(scene_path: String, transition: TransitionType = TransitionType.FADE_BLACK) -> void:
    match transition:
        TransitionType.FADE_BLACK:
            # Fade out (0.15s) → troca de cena → fade in (0.15s)
            await _fade_to(Color.BLACK, 0.15)
            get_tree().change_scene_to_file(scene_path)
            await get_tree().process_frame  # aguarda cena carregar
            await _fade_to(Color.TRANSPARENT, 0.15)

        TransitionType.SLASH_HORIZONTAL:
            # Wipe com textura de jornal rasgado (estilo André Guedes)
            await _play_wipe_animation()
            get_tree().change_scene_to_file(scene_path)
            await _play_wipe_reverse()

        TransitionType.INSTANT:
            get_tree().change_scene_to_file(scene_path)
```

**Mapa de transições:**

| De → Para | Tipo | Duração total |
|---|---|---|
| Menu → Weapon Select | Slash horizontal | 0.3s |
| Weapon Select → Gameplay | Fade black | 0.3s |
| Gameplay → Game Over | Fade black lento | 0.5s |
| Game Over → Menu | Fade black | 0.3s |
| Game Over → Gameplay (revive) | Fade branco rápido | 0.2s |

### Layout Responsivo — Aspect Ratios

O A06 tem 720×1600 (20:9). Outros devices variam:

```gdscript
# src/utils/layout_utils.gd
static func get_safe_area_bottom() -> float:
    # Android navigation bar height
    return DisplayServer.get_display_safe_area().position.y

static func setup_hud_for_aspect_ratio(hud: Control) -> void:
    var viewport_size := Vector2(
        ProjectSettings.get("display/window/size/viewport_width"),
        ProjectSettings.get("display/window/size/viewport_height")
    )
    var aspect := viewport_size.x / viewport_size.y

    # Para telas mais longas (>18:9), adiciona padding no bottom
    if aspect < (9.0 / 18.0):  # mais que 18:9
        hud.get_node("BottomBar").add_theme_constant_override("margin_bottom", 24)
```

**Project Settings — Stretch Mode:**
- `display/window/stretch/mode` = `canvas_items`
- `display/window/stretch/aspect` = `expand`
- Viewport base: 720×1280 (16:9) — expande para cima/baixo em telas mais longas

---

## 6. Audio System

### Arquitetura de Buses

```
AudioServer Buses:
├── Master (volume global)
│   ├── SFX_Combat (compressor leve — evita clipping em combo)
│   │   ├── Impacts (hit sounds, armas)
│   │   └── Deaths (sons de morte, falas dos zumbis)
│   ├── SFX_UI (volume padrão — clicks, transições)
│   ├── SFX_Ambient (volume baixo — vento, ambiente Brasília)
│   └── Music (volume separado do SFX)
│       ├── Music_Gameplay (loop principal)
│       └── Music_Boss (tocado por cima ou substitui)
```

### AudioManager — Sistema de Prioridade

O maior risco em mobile é empilhar AudioStreamPlayer demais e causar clipping ou overhead. Solução: pool de players com prioridade:

```gdscript
# src/autoloads/audio_manager.gd
class_name AudioManager extends Node

const MAX_CONCURRENT_SFX: int = 8       # A06 aguenta bem 8 simultâneos
const MAX_COMBAT_SFX: int = 4           # máx de sons de combate simultâneos

var _sfx_players: Array[AudioStreamPlayer2D] = []
var _combat_count: int = 0

func _ready() -> void:
    # Pre-aloca players no pool
    for i in MAX_CONCURRENT_SFX:
        var player := AudioStreamPlayer2D.new()
        player.bus = "SFX_Combat"
        add_child(player)
        _sfx_players.append(player)
        player.finished.connect(func(): _combat_count -= 1 if _combat_count > 0 else 0)

func play_sfx_at(stream: AudioStream, pos: Vector2, pitch: float = 1.0, is_combat: bool = true) -> void:
    # Throttle: se já temos muitos sons de combate simultâneos, descarta
    if is_combat and _combat_count >= MAX_COMBAT_SFX:
        return

    var player := _get_free_player()
    if player == null:
        return  # sem player disponível — descarta som (melhor que travar)

    player.stream = stream
    player.pitch_scale = pitch
    player.global_position = pos
    player.play()
    if is_combat:
        _combat_count += 1

func play_sfx_ui(stream: AudioStream) -> void:
    # Sons de UI vão para bus separada, não competem com combate
    $UIPlayer.stream = stream
    $UIPlayer.play()
```

### Spatial Audio Simplificado

Para 2D mobile, spatial audio completo é overhead desnecessário. Implementação simples:

```gdscript
# Volume por distância do player — calculado no AudioStreamPlayer2D
# attenuation_filter_cutoff_hz e max_distance configurados no inspector:
# max_distance = 600px (além disso, volume = 0)
# attenuation = 1 (linear) — mais previsível que exponencial
```

### Sistema de Música — Adaptive

A música adapta conforme o estado do jogo sem crossfade brusco:

```gdscript
# src/autoloads/audio_manager.gd
func set_music_state(state: String) -> void:
    match state:
        "menu":
            _crossfade_to($MusicMenu, 1.5)
        "gameplay":
            _crossfade_to($MusicGameplay, 0.5)
        "boss":
            # Boss music sobrepõe gameplay music (não substitui)
            $MusicBoss.volume_db = -20.0
            $MusicBoss.play()
            var tween := create_tween()
            tween.tween_property($MusicBoss, "volume_db", 0.0, 1.0)
            tween.parallel().tween_property($MusicGameplay, "volume_db", -10.0, 1.0)
        "boss_dead":
            # Triunfo por 3s, depois volta ao gameplay
            await get_tree().create_timer(3.0).timeout
            set_music_state("gameplay")

func _crossfade_to(target: AudioStreamPlayer, duration: float) -> void:
    var tween := create_tween()
    for player in [$MusicMenu, $MusicGameplay, $MusicBoss]:
        if player != target:
            tween.parallel().tween_property(player, "volume_db", -60.0, duration)
    if not target.playing:
        target.play()
    tween.parallel().tween_property(target, "volume_db", 0.0, duration)
```

### Prioridade de SFX em Situações de Alta Intensidade

Quando combo está alto e muitos zumbis morrem simultaneamente, a fila de SFX seria barulhenta demais. Regras de throttle:

| Situação | Regra |
|---|---|
| Combo ≥ 10 | Sons de morte individual suprimidos (80% das kills não tocam morte SFX) |
| ≥ 4 hits simultâneos | Apenas o hit de maior dano toca SFX |
| Boss vivo | Sons de zumbis básicos reduzem volume para -6dB |
| Receber dano | Prioridade máxima — sempre toca (feedback crítico) |

---

## 7. Particle System

### Budget de Partículas por Frame

No A06 com Helio G85, o target é manter partículas abaixo de **300 partículas ativas simultâneas** para garantir 60fps:

| Tipo | Partículas máx | Pool size | Lifetime |
|---|---|---|---|
| Impacto de hit (pó/sangue) | 8 por hit | 20 instâncias | 0.4s |
| Morte de zumbi básico | 12 por morte | 15 instâncias | 0.8s |
| Morte de zumbi médio | 18 por morte | 8 instâncias | 1.0s |
| Morte de boss | 60 (one-shot) | 2 instâncias | 2.0s |
| Papéis/press releases | 10 por morte (Assessor) | 10 instâncias | 1.5s |
| Power-up brilho | 6 (loop enquanto existe) | 10 instâncias | loop |
| Combo ≥ 10 | 15 (burst) | 5 instâncias | 0.6s |
| Score gigante (boss kill) | 40 (chuva de confetes) | 1 instância | 2.5s |
| **Total simultâneo máx** | **~250** | — | — |

### Implementação com CPUParticles2D vs GPUParticles2D

| Tipo de Partícula | Sistema | Justificativa |
|---|---|---|
| Papéis (sprites customizados) | CPUParticles2D | Precisa de texture personalizada de papel |
| Pó/Sangue (pontos/sprites) | GPUParticles2D | GPU é mais eficiente para count alto |
| Confetes do boss | GPUParticles2D | 40 partículas, burst único |
| Brilho de power-up | GPUParticles2D | Loop contínuo, baixo count |

### LOD de Partículas para Devices Low-End

`RemoteConfig` controla `particle_quality_low_end` (0.5 por padrão no A06):

```gdscript
# src/utils/particle_lod.gd
class_name ParticleLOD extends Node

static func apply_quality(particles: GPUParticles2D) -> void:
    var quality: float = RemoteConfigManager.get_float("particle_quality_low_end", 1.0)
    particles.amount = max(1, int(particles.amount * quality))
    if quality <= 0.5:
        # No low-end, desativa partículas de pó de impacto (mantém só morte)
        if particles.is_in_group("impact_dust"):
            particles.emitting = false
```

### Partículas de Papel — Implementação Específica

Papéis que voam (morte do Assessor, urna, etc.) precisam de rotação e gravidade, não partículas puras:

```gdscript
# Nó manual: Node2D com script de física simples
# Mais expressivo e controlável que sistema de partículas
class_name FlyingPaper extends Node2D

var velocity: Vector2
var angular_velocity: float
var gravity: float = 200.0
var lifetime: float = 1.5
var _elapsed: float = 0.0

func launch(direction: Vector2, speed: float) -> void:
    velocity = direction * speed + Vector2(randf_range(-50, 50), randf_range(-100, -50))
    angular_velocity = randf_range(-360.0, 360.0)  # graus/s

func _physics_process(delta: float) -> void:
    _elapsed += delta
    if _elapsed >= lifetime:
        PoolManager.release_paper(self)
        return
    velocity.y += gravity * delta
    position += velocity * delta
    rotation_degrees += angular_velocity * delta
    modulate.a = 1.0 - (_elapsed / lifetime)  # fade out
```

---

## 8. Performance Budget

### Frame Budget Completo — 16.6ms (60fps)

Breakdown detalhado para o A06 (Helio G85 — single core ~2.0GHz efetivo):

```
TOTAL BUDGET: 16.6ms
│
├── [2.0ms]  Physics (move_and_slide) — Player + até 25 zumbis
│            NavigationAgent2D de todos os zumbis ativos
│            CollisionShape2D checks (HurtboxArea)
│
├── [3.0ms]  AI dos Zumbis — StateMachine updates
│            Pathfinding (NavigationAgent2D.get_next_path_position)
│            Behavior logic (chase, attack decisions)
│
├── [1.5ms]  Combat System — damage calculation, hit checks
│            ScoreSystem, LootSystem updates
│            Combo timer update
│
├── [4.0ms]  Rendering — Godot CanvasRenderer
│            Draw calls: target ≤ 35 draw calls por frame
│            Sprite batching (mesmo material/textura agrupado)
│            Shader passes (vignette, color grading)
│
├── [2.0ms]  Particle Systems — CPUParticles2D update
│            Flying paper physics
│            GPUParticles2D command submission
│
├── [1.0ms]  UI (HUD) — CanvasLayer rendering
│            Label updates (score, combo — throttled, max 10x/s)
│            Tween updates
│
├── [1.5ms]  Audio — AudioServer mixing
│            8 players simultâneos, resampling
│
├── [1.0ms]  Overhead — GDScript GC, signal dispatch
│            PoolManager checks
│            RemoteConfig reads (cache, sem I/O)
│
└── [1.6ms]  Buffer — margem de segurança (~10%)
```

### Draw Calls — Target ≤ 35

Estratégia para manter baixo:

| Categoria | Draw Calls | Estratégia |
|---|---|---|
| TileMap (chão) | 1-2 | Single atlas, Godot batching automático |
| ParallaxBackground (3 layers) | 3 | Texturas únicas por layer |
| Zumbis (até 25) | 4-6 | Mesmo SpriteFrames → mesmo material → batch |
| Player | 1 | |
| Projéteis (até 20) | 1-2 | Pool com mesma textura |
| VFX/partículas | 3-4 | Agrupados por material |
| HUD | 5-8 | CanvasLayer separada |
| Pickups (até 10) | 1-2 | Same atlas |
| Sombras | 1-2 | Single shader, batch |
| **Total** | **~24-32** | Margem até 35 |

**Regra de batching:** Sprites com o mesmo `Texture2D` e mesmo `Material` são batched automaticamente pelo Godot Compatibility Renderer. Manter todos os zumbis de um tipo com o mesmo atlas é a otimização mais fácil.

### Memory Budget

| Sistema | RAM Target | Notas |
|---|---|---|
| Texturas de sprites (atlases) | 80MB | 8 atlases de ~2048×2048 RGBA8 = ~128MB descomprimido, ~64MB com ETC2 |
| Audio em memória (SFX frequentes) | 20MB | Sons de hit/morte pré-carregados; música em streaming |
| Cenas instanciadas (pool) | 15MB | ~75 objetos no pool, cada um ~200KB |
| GDScript runtime + sistemas | 10MB | |
| Firebase SDK + buffer de rede | 8MB | |
| Android/Java overhead | 50MB | Inevitável no Android |
| **Total estimado** | **~183MB** | Margem confortável no A06 (4GB, ~2.5GB disponível para apps) |

---

## 9. Asset Specs

### Sprite Sheets — Formato e Tamanho

**Regra geral:** 1 atlas PNG por entidade principal. Máximo 2048×2048 por atlas (garantido em todos os GPUs com OpenGL ES 3.0).

| Entidade | Atlas Size | Frames estimados | Bytes (ETC2) |
|---|---|---|---|
| Player | 1024×512 | 24 frames (todas as animações) | ~256KB |
| Vereador | 512×512 | 16 frames | ~128KB |
| Assessor | 512×512 | 18 frames | ~128KB |
| Senador Vitalício | 1024×512 | 20 frames (animação de tombamento longa) | ~256KB |
| Lobista | 512×512 | 16 frames | ~128KB |
| Ministra | 512×256 | 12 frames | ~64KB |
| Candidato Eterno (Boss) | 2048×1024 | 40 frames (todas as fases) | ~1MB |
| Fantasma | 512×512 | 14 frames (semi-transparente) | ~128KB |
| UI/Ícones Atlas | 1024×1024 | todos ícones de HUD, botões | ~512KB |
| VFX/Onomatopeias | 512×256 | THWACK, SLAP, BOOM, WHAM, WHOOSH | ~64KB |

**Formato:** PNG para import no Godot → exportar como **ETC2** para Android (hardware compression, 4:1 ratio). O A06 tem suporte garantido a ETC2.

**Importação no Godot:**
- `Compress/Mode` = `ETC2`
- `Mipmaps/Generate` = `false` (sprites 2D não precisam de mipmaps)
- `Filter` = `Nearest` (estilo pixel/HQ, não bilinear que borraria)
- `Repeat` = `Disabled`

### Audio — Formatos

| Tipo | Formato | Bitrate/Quality | Notas |
|---|---|---|---|
| SFX curtos (< 1s) | OGG Vorbis | 96kbps | Pré-carregado em memória |
| SFX médios (1-3s) | OGG Vorbis | 96kbps | Pré-carregado |
| Música em loop | OGG Vorbis | 128kbps | **Streaming** — não carrega inteiro |
| Falas dos zumbis | OGG Vorbis | 64kbps | Pool de 3-5 variações por zumbi |

**Tamanho total de áudio estimado:** ~8MB comprimido (sem música em streaming).

### Fontes

| Fonte | Arquivo | Tamanho | Uso |
|---|---|---|---|
| Bebas Neue Bold | `bebas_neue_bold.ttf` | ~50KB | Score, wave, headlines |
| Oswald Regular | `oswald_regular.ttf` | ~60KB | UI geral, menus |
| Fonte manuscrita | `hq_irregular.ttf` | ~80KB | Falas zumbis, flavor text |

Carregar todas as 3 como `DynamicFont` com **pre-render de bitmap** nas sizes usadas (18sp, 22sp, 28sp) para evitar rasterização em runtime.

---

## 10. Shader Effects

### Filosofia: Shaders Simples, Impacto Alto

OpenGL ES 3.0 no A06 suporta fragment shaders eficientemente. A regra é: **cada shader deve fazer UMA coisa, fazer bem, e ser barato**.

### Shader 1 — Vignette + Color Grading (Post-Process Global)

Aplicado como `CanvasLayer` com `ColorRect` cobrindo a tela inteira:

```glsl
// assets/shaders/post_process.gdshader
shader_type canvas_item;

uniform float vignette_strength: hint_range(0.0, 1.0) = 0.35;
uniform float saturation: hint_range(0.0, 2.0) = 1.15;  // ligeiro boost
uniform vec4 color_tint: source_color = vec4(1.0, 0.98, 0.92, 1.0);  // leve amarelado

void fragment() {
    vec2 uv = SCREEN_UV;

    // Vignette
    vec2 center = uv - 0.5;
    float vignette = 1.0 - dot(center, center) * vignette_strength * 2.5;

    // Color grading — paleta André Guedes
    vec4 color = texture(TEXTURE, UV);
    float gray = dot(color.rgb, vec3(0.299, 0.587, 0.114));
    color.rgb = mix(vec3(gray), color.rgb, saturation);
    color.rgb *= color_tint.rgb;
    color.rgb *= vignette;

    COLOR = color;
}
```

**Custo estimado:** ~0.3ms por frame (CanvasItem simples, operações lineares).

### Shader 2 — Hit Flash Branco (Sprite Material)

Material reutilizado em todos os sprites de entidades:

```glsl
// assets/shaders/hit_flash.gdshader
shader_type canvas_item;

uniform float flash_amount: hint_range(0.0, 1.0) = 1.0;

void fragment() {
    vec4 color = texture(TEXTURE, UV);
    if (color.a < 0.01) discard;
    // Mix para branco
    color.rgb = mix(color.rgb, vec3(1.0), flash_amount);
    COLOR = color;
}
```

**Uso:** Criado uma vez como `ShaderMaterial`, setado em `$AnimatedSprite2D.material` durante o flash, removido após. Custo zero quando não ativo.

### Shader 3 — Transparência do Fantasma

```glsl
// assets/shaders/ghost_transparency.gdshader
shader_type canvas_item;

uniform float ghost_alpha: hint_range(0.0, 1.0) = 0.55;
uniform float flicker_speed: hint_range(0.0, 10.0) = 3.0;

void fragment() {
    vec4 color = texture(TEXTURE, UV);
    // Flickering baseado em TIME
    float flicker = 0.8 + sin(TIME * flicker_speed) * 0.2;
    color.a *= ghost_alpha * flicker;
    COLOR = color;
}
```

### Shader 4 — Damage Flash da Tela

`ColorRect` no topo do CanvasLayer do HUD, visível apenas ao tomar dano:

```glsl
// assets/shaders/screen_flash.gdshader
shader_type canvas_item;
// Simples: controle apenas via modulate.a do ColorRect
// Cor vermelha (#8B1A1A) definida no ColorRect
// Alpha animado via Tween — zero custo de shader
void fragment() {
    COLOR = COLOR;  // pass-through, controle via modulate
}
```

### Shader 5 — Cooldown Arc (Botão de Ataque)

Para o arco de cooldown visual no botão de ataque, um CustomDraw é mais eficiente que shader:

```gdscript
# src/ui/cooldown_arc.gd
class_name CooldownArc extends Control

var progress: float = 1.0  # 0.0 = vazio, 1.0 = cheio

func _draw() -> void:
    var center := size / 2.0
    var radius := min(size.x, size.y) * 0.45
    var start_angle := -PI / 2.0  # topo
    var end_angle := start_angle + (TAU * progress)

    # Fundo escuro
    draw_arc(center, radius, 0, TAU, 32, Color(0, 0, 0, 0.5), 4.0)
    # Arco de progresso
    if progress > 0.01:
        draw_arc(center, radius, start_angle, end_angle, 32, Color("#C8B84A"), 4.0)

func set_progress(value: float) -> void:
    progress = clamp(value, 0.0, 1.0)
    queue_redraw()
```

---

## 11. Otimizações para Low-End

### Estratégia: Detectar, Degradar com Elegância

O A06 é nosso device target, mas pode haver devices ainda mais fracos. A filosofia é: **o jogo nunca deve ser injogável, apenas menos bonito**.

### Detecção de Capacidade do Device

```gdscript
# src/autoloads/game_state.gd
enum DeviceTier { HIGH, MEDIUM, LOW }

var device_tier: DeviceTier = DeviceTier.MEDIUM

func _detect_device_tier() -> void:
    var ram_mb := OS.get_memory_info().get("physical", 0) / 1_000_000
    var cpu_count := OS.get_processor_count()

    if ram_mb >= 6000 and cpu_count >= 6:
        device_tier = DeviceTier.HIGH
    elif ram_mb >= 3000 and cpu_count >= 4:
        device_tier = DeviceTier.MEDIUM  # A06 cai aqui
    else:
        device_tier = DeviceTier.LOW
```

### Configurações por Tier

| Feature | HIGH | MEDIUM (A06) | LOW |
|---|---|---|---|
| Partículas | 100% | 100% | 50% |
| Screen shake | Completo | Completo | Reduzido 50% |
| Parallax layers | 4 | 4 | 2 (remove árvores e chão) |
| Sombras | Sim | Sim | Não |
| Post-process shader | Completo | Completo | Desativado |
| Ghost shader (Fantasma) | Sim | Sim | Substituído por alpha simples |
| Max zumbis em tela | 30 | 25 | 15 |
| NavigationAgent2D updates | Cada frame | Cada frame | A cada 2 frames |
| Flying paper (partículas físicas) | Sim | Sim | Substituído por GPUParticles simples |

### Culling — Fora da Câmera

```gdscript
# Em zombie_base.gd — desativa processamento quando fora da câmera
func _on_visibility_changed() -> void:
    set_physics_process(is_visible_in_tree())
    # IA (pathfinding) continua rodando mesmo fora da câmera — só animação pausa
    $AnimatedSprite2D.pause()  if not is_visible_in_tree() else $AnimatedSprite2D.play()
```

**VisibilityEnabler2D:** Adicionar `VisibilityEnabler2D` em cada prefab de zumbi com:
- `enable_physics_process = true`
- `enable_process = false` (AI continua via signals, não _process)
- `physics_process_parent = true`

### Resolução Dinâmica

Se o framerate cair abaixo de 50fps por 3 segundos seguidos:

```gdscript
# src/autoloads/game_state.gd
var _fps_samples: Array[float] = []
const FPS_SAMPLE_SIZE: int = 180  # 3 segundos a 60fps
var _resolution_scale: float = 1.0

func _process(delta: float) -> void:
    _fps_samples.append(Engine.get_frames_per_second())
    if _fps_samples.size() > FPS_SAMPLE_SIZE:
        _fps_samples.pop_front()
        var avg_fps := _fps_samples.reduce(func(acc, v): return acc + v, 0.0) / FPS_SAMPLE_SIZE
        if avg_fps < 50.0 and _resolution_scale > 0.75:
            _resolution_scale -= 0.05
            get_viewport().content_scale_factor = _resolution_scale
        elif avg_fps > 58.0 and _resolution_scale < 1.0:
            _resolution_scale = min(1.0, _resolution_scale + 0.025)
            get_viewport().content_scale_factor = _resolution_scale
```

### Pool de Navegação — Throttle de Pathfinding

Pathfinding é caro. Com 25 zumbis, executar `get_next_path_position()` todo frame seria ~2ms extras. Solução: stagger os updates:

```gdscript
# Em zombie_base.gd
var _nav_update_interval: float = 0.15  # atualiza rota a cada 150ms
var _nav_timer: float = 0.0

func _physics_process(delta: float) -> void:
    _nav_timer += delta
    if _nav_timer >= _nav_update_interval:
        _nav_timer = 0.0
        _update_navigation()
    # Movimento usa o último target calculado (não recalcula cada frame)
    move_and_slide()
```

---

## 12. Implementação dos 7 Zumbis

### Zumbi 1: Vereador (Tier: BASIC)

**Papel no design:** Tutorial vivo. Ensina movimento e ataque sem punir.

**Especificações de Animação:**

| Animação | Frames | FPS | Notas |
|---|---|---|---|
| idle | 2 | 4 | Movimento lento, gravata balançando |
| walk | 4 | 10 | Passo arrastado, braços estendidos |
| attack | 3 | 12 | Abraçar/morder — engraçado, não assustador |
| hurt | 2 | 12 | Expressão de ofensa, não dor |
| death | 6 | 10 | Cai dramaticamente com papéis voando |

**VFX na Morte:**
- 4-6 papéis de lei voam para cima (FlyingPaper × 5, direção: para cima com spread)
- 2-3 notas de cédula (sprites de papel rasgado, escala pequena)
- Crachá de vereador voa para lateral com rotação rápida (1 sprite único)
- Pó laranja no ponto de impacto (GPUParticles2D, 8 partículas, burst, lifetime 0.4s)
- Onomatopeia: "THWACK" (vassoura) / "SLAP" (chinelo)

**SFX:**
- Hit: `sfx_hit_flesh_light.ogg` + pitch random (0.9 - 1.1)
- Morte: `sfx_body_fall_light.ogg`
- Fala de morte (40% chance): `sfx_vereador_death_01.ogg` — "Fui eleito democraticamente!" / "Protocolo de urgência!"

**AI:** Chase simples — NavigationAgent2D direto ao player. Sem comportamento especial.

**Stats base:** HP: 30, velocidade: 55px/s, dano: 1, score: 50

---

### Zumbi 2: Assessor de Comunicação (Tier: MEDIUM)

**Papel no design:** Ensina esquiva. Primeiro projétil que o jogador recebe.

**Especificações de Animação:**

| Animação | Frames | FPS | Notas |
|---|---|---|---|
| idle | 2 | 6 | Mãos ocupadas com prancheta |
| walk_zigzag | 6 | 12 | Loop que alterna direção naturalmente |
| throw_release | 4 | 18 | Wind-up rápido + lançamento de press release |
| throw_loop | 3 | 12 | Enquanto em modo "ataque à distância" |
| hurt | 2 | 12 | |
| death | 5 | 10 | Cai jogando papers para cima |

**VFX na Morte:**
- 8-10 press releases explodem em leque (FlyingPaper × 9, ângulos de -60° a +60° acima)
- Câmera invisível "estala" (sprite flash branco de câmera, 2 frames)
- 2-3 papéis flutuam devagar para baixo (FlyingPaper com gravidade reduzida)
- Pó cinza no ponto de impacto

**SFX:**
- Lançamento de projétil: `sfx_paper_whoosh.ogg`
- Hit no player: `sfx_paper_slap.ogg`
- Morte: `sfx_paper_explosion.ogg` (burst de papéis)
- Fala de morte: "A mídia está distorcendo!" / "Isso é narrativa!"

**Projétil (press release voador):**
- Sprite: papel A4 amassado, rotação de 360°/s
- Velocidade: 180px/s
- Dano: 1
- Alcance máximo: 350px antes de desaparecer

**AI:** Zigzag — alterna para lados a cada 1.5s. Ataca de longa distância (300px). Se player chega a 100px, recua.

**Stats base:** HP: 20, velocidade: 75px/s (zigzag), dano: 1 (projétil), score: 80

---

### Zumbi 3: Senador Vitalício (Tier: TANK)

**Papel no design:** Ensina que nem tudo pode ser atacado frontalmente. Kiting obrigatório.

**Especificações de Animação:**

| Animação | Frames | FPS | Notas |
|---|---|---|---|
| idle | 3 | 4 | Bengala batendo no chão ritualmente |
| walk_slow | 4 | 8 | Muito devagar, imponente |
| immune_pose | 2 | 6 | Loop durante imunidade — expressão altiva |
| rush | 4 | 16 | A 10% HP: corre em direção ao player |
| attack | 3 | 10 | Bengalada lenta mas devastadora |
| hurt | 2 | 8 | Expressão de ultraje, não dor |
| death | 10 | 8 | Tombamento lento e dramático (0.8s) |

**VFX na Morte:**
- Bengala voa para um lado com rotação lenta (1 sprite, FlyingPaper adaptado)
- Distintivo dourado sobe com brilho (GPUParticles2D, 3 partículas radiais, brilho)
- Confetes de "votação" — estrelinhas em vermelho e amarelo (GPUParticles2D, 15 partículas)
- Smoke pesado cinza no ponto de tombamento (CPUParticles2D, 10 partículas, lifetime 1.0s)
- Screen shake adicional: `Camera.add_trauma(0.3)` (tombamento pesado)

**Efeito de Imunidade:**
- Shader de outline pulsante dourado ao redor do sprite (ShaderMaterial separado)
- Som de "campainha de votação" em loop suave durante imunidade

**SFX:**
- Hit: `sfx_hit_heavy.ogg` (som de madeira de bengala)
- Imunidade ativa: `sfx_immunity_bell.ogg`
- Rush: `sfx_senator_rush.ogg` (respiração pesada + passos rápidos)
- Morte: `sfx_heavy_fall.ogg` + `sfx_senate_bell_final.ogg`
- Fala de morte: "Tenho imunidade!" / "Serei lembrado pela história!"

**AI:** Perseguição lenta. A 50% HP: para por 3s (imunidade — invulnerável). A 10% HP: velocidade ×1.8, carga direta.

**Stats base:** HP: 120, velocidade: 40px/s (normal) / 72px/s (rush), dano: 3, score: 200

---

### Zumbi 4: Lobista (Tier: ESPECIAL/SUPORTE)

**Papel no design:** Ensina a priorizar alvos. Buffa os outros — deve ser morto primeiro.

**Especificações de Animação:**

| Animação | Frames | FPS | Notas |
|---|---|---|---|
| idle | 3 | 6 | Mexe no celular enquanto caminha |
| walk_flank | 4 | 10 | Tenta flanquear — movimentação lateral |
| buff_cast | 5 | 12 | Anima "deal" — aperto de mão no ar |
| buff_active | 2 | 6 | Loop — aura dourada ao redor |
| hurt | 2 | 12 | |
| death | 5 | 10 | Celular voa longe, expressão de traição |

**VFX na Morte:**
- Celular voa em arco (FlyingPaper adaptado com sprite de celular)
- Cédulas de dinheiro voam em todas as direções (GPUParticles2D, 8 partículas, sprites de cédula)
- Aura de buff se dissolve (CPUParticles2D radial, 12 partículas douradas, burst)
- Zumbis próximos perdem o buff: efeito visual de "apagamento" neles (flash de desatualizacão)

**Aura de Buff:**
- Círculo de radius 150px ao redor do Lobista (sempre visível enquanto vivo)
- Sprite de aura: anel amarelo semi-transparente, rotação lenta
- Zumbis dentro da aura: +30% velocidade, outline amarelo sutil

**SFX:**
- Buff ativado: `sfx_money_clink.ogg`
- Morte: `sfx_briefcase_drop.ogg` + `sfx_deal_cancelled.ogg`
- Fala de morte: "O contrato era claro!" / "Eu só estava facilitando!"

**AI:** Nunca vai direto ao player. Calcula posição 90° lateral. Mantém distância de 200px. Buffa automaticamente todo zumbi em raio.

**Stats base:** HP: 40, velocidade: 65px/s, dano: 1 (toque), score: 150

---

### Zumbi 5: Ministra (Tier: SUPORTE/ESPECIAL)

**Papel no design:** Controle de área. O jogador aprende que alguns inimigos são mais perigosos parados do que em movimento.

**Especificações de Animação:**

| Animação | Frames | FPS | Notas |
|---|---|---|---|
| idle | 3 | 5 | Gesto de oratória, não se move muito |
| walk_slow | 3 | 8 | Caminha apenas para posicionar zona |
| cast_zone | 6 | 10 | Gesto de "corte de orçamento" — braços cruzados |
| zone_active | 2 | 6 | Loop — expressão satisfeita |
| hurt | 2 | 10 | |
| death | 5 | 10 | Pastas voam, expressão de dignidade ofendida |

**VFX da BudgetCutZone:**
- Círculo vermelho transparente no chão (raio 80px) — `Line2D` desenhado como círculo com fill
- Ícones de "corte" (tesoura pixel art) pulsam dentro da zona
- Player dentro da zona: vinheta vermelha extra + drain de HP de 0.5/s

**VFX na Morte:**
- 4-6 pastas ministeriais voam (FlyingPaper × 5 com sprites de pasta)
- Confetes de "proposta reprovada" (papéis picados, GPUParticles2D)
- BudgetCutZone existente se dissolve instantaneamente

**SFX:**
- Zona criada: `sfx_budget_cut.ogg` (som de tesoura + som burocrático)
- Player na zona: `sfx_drain_loop.ogg` (som contínuo, baixo volume)
- Morte: `sfx_folders_drop.ogg`
- Fala de morte: "Isso é responsabilidade fiscal!" / "Não existe almoço grátis!"

**AI:** Posiciona em tiles de alto tráfego do player. Não persegue. Cria zona a cada 5s.

**Stats base:** HP: 35, velocidade: 30px/s, dano: 0 (não ataca diretamente), score: 120

---

### Zumbi 6: Candidato Eterno (BOSS — Tier: BOSS)

**Papel no design:** Pico emocional da sessão. Usa tudo que o jogador aprendeu. Duas fases — o "Segundo Turno" é o momento de maior tensão.

**Especificações de Animação:**

| Animação | Frames | FPS | Notas |
|---|---|---|---|
| entrance | 8 | 10 | Caminha da borda com tema musical |
| idle_boss | 4 | 6 | Sorriso impossível, braços abertos |
| phase1_chase | 4 | 8 | Caminhada rápida mas digna |
| discurso_windup | 6 | 12 | Microfone levantado, aura cresce |
| discurso_blast | 4 | 18 | AOE de discurso — onda de som |
| invoke_adds | 5 | 10 | Chama zumbis de "cabo eleitoral" |
| segundo_turno | 8 | 14 | Levantar do chão — mais rápido, mais raivoso |
| phase2_rush | 4 | 16 | Fase 2: corre diretamente |
| phase2_slam | 5 | 14 | Ataque de area de fase 2 |
| death_final | 12 | 8 | Morte épica — 0.8s de animação longa |

**Sistema de Fases:**

```gdscript
# src/entities/zombies/zombie_candidato.gd
enum Phase { NORMAL, DISCURSO, INVOKE_ADDS, SEGUNDO_TURNO }

var current_phase: Phase = Phase.NORMAL
var segundo_turno_triggered: bool = false

func _on_hp_changed() -> void:
    var hp_pct := float(current_hp) / float(max_hp)

    if hp_pct <= 0.66 and current_phase == Phase.NORMAL:
        _enter_discurso_phase()
    elif hp_pct <= 0.33 and current_phase != Phase.SEGUNDO_TURNO:
        if not segundo_turno_triggered:
            _trigger_segundo_turno()  # "morre" e levanta
    elif hp_pct <= 0.0 and segundo_turno_triggered:
        _trigger_final_death()

func _trigger_segundo_turno() -> void:
    segundo_turno_triggered = true
    # "Morre" temporariamente
    $AnimatedSprite2D.play("death_fake")
    Engine.time_scale = 0.3  # mini hitstop dramático
    await get_tree().create_timer(0.5, true).timeout
    Engine.time_scale = 1.0
    # Levanta com animação e cura 40% do HP
    current_hp = int(max_hp * 0.4)
    $AnimatedSprite2D.play("segundo_turno")
    AudioManager.play_sfx(preload("res://assets/audio/sfx/sfx_segundo_turno.ogg"))
    current_phase = Phase.SEGUNDO_TURNO
```

**VFX na Morte Final:**
- `Engine.time_scale = 0.0` por 18 frames (pausa dramática de 0.3s)
- Flash branco na tela inteira (modulate do CanvasLayer vai para branco e volta)
- Explosão de bandeiras rasgadas (GPUParticles2D, 60 partículas, direções todas)
- Score gigante aparece no centro: "CANDIDATO DERROTADO — 0 VOTOS"
- Chuva de confetes por 2 segundos (GPUParticles2D, 40 partículas, duração 2.0s)
- Screen shake: `Camera.add_trauma(0.7)` — o maior do jogo
- SFX especial: `sfx_boss_death_apuracao.ogg` (apuração eleitoral distorcida + multidão)

**Haptic:** Padrão de 3 pulsos crescentes: 50ms → pausa 100ms → 80ms → pausa 80ms → 120ms

**Discurso AOE:**
- Onda circular que emana do boss (raio crescente, sprite de ring)
- Dano: 2 ao player se atingido
- Visual: anel de texto político ilegível se expande e dissolve

**Stats base:** HP: 400 (fase 1: 60%, fase 2: 40%), velocidade: 55px/s (F1) / 90px/s (F2), dano: 3, score: 2000

---

### Zumbi 7: Fantasma Parlamentar (Tier: ESQUIVO)

**Papel no design:** Debuff e frustração táticas. Aprende que nem todo inimigo deve ser atacado diretamente.

**Especificações de Animação:**

| Animação | Frames | FPS | Notas |
|---|---|---|---|
| idle | 3 | 5 | Flutua levemente (oscillação senoidal na posição Y) |
| float_chase | 4 | 8 | Travessia direta — atravessa obstáculos |
| phase_in | 4 | 12 | Materialização — vai de 0% para 55% alpha |
| phase_out | 4 | 12 | Desmaterialização ao ser atingido |
| debuff_touch | 3 | 14 | Contato que aplica debuff |
| death | 6 | 10 | Dissolve-se em partículas — não cai |

**Física Especial:**
- Atravessa obstáculos (`set_collision_mask_value(2, false)` — ignora layer de obstáculos)
- Não usa NavigationAgent2D — vai em linha reta
- Flutua verticalmente: `position.y += sin(Time.get_ticks_msec() / 500.0) * 0.5`

**Shader de Transparência:** `ghost_transparency.gdshader` (ver seção 10). Alpha de 55% + flickering.

**Debuff aplicado ao Player:**
- Velocidade do player reduz em 30% por 4 segundos
- Visual: vinheta levemente azul-esverdeada na tela (ColorRect, alpha 0.2)
- SFX: `sfx_debuff_ghost.ogg` (som etéreo, baixo volume)

**VFX na Morte:**
- Sem papéis ou objetos físicos — o fantasma é burocrático, não material
- Dissolução: partículas de energia (GPUParticles2D, 15 partículas brancas/azuis, burst radial)
- Cura do player de 15% HP (único inimigo que cura ao morrer — comentário sobre impunidade)
- SFX: `sfx_ghost_dissolve.ogg` + "Serei reconduzido!"

**AI:** Atravessa tudo, vai direto ao player. Prioriza jogadores com debuff ativo (não aplica duplo debuff — espera o primeiro expirar).

**Stats base:** HP: 25, velocidade: 80px/s (ignora colisão), dano: 0 (debuff, não HP), score: 100

---

## Resumo de Prioridade de Implementação

Para a Sprint 1-2 do roadmap, a ordem de implementação que maximiza feedback rápido:

```
Sprint 1 (semanas 1-3):
1. Touch Input System completo (joystick + ataque + auto-aim)
2. AnimatedSprite2D do player com idle/run/attack
3. Vereador básico (AI simples + morte com 3 VFX)
4. Hit stop + hit flash (game feel fundamental)
5. HUD básico (corações + score sem animação)

Sprint 2 (semanas 4-6):
1. Screen shake + damage numbers
2. Assessor + projétil
3. HUD completo com animações
4. Onomatopeias visuais
5. AudioManager com 8 SFX básicos

Sprint 3 (semanas 7-9):
1. Todos os zumbis restantes
2. Particle systems completos
3. Post-process shader (vignette)
4. Transições de cena
5. Performance profiling no A06 real
```

---

*Document Version 1.0 — Abril 2026*
*"O segredo do game feel não é magia. É trabalho deliberado em cada frame, cada som, cada pixel. Quando está certo, o jogador não percebe — apenas sente que não consegue parar de jogar."*
