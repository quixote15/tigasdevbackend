#!/usr/bin/env python3
"""
Build a SIDE-VIEW preview of the Esplanada dos Ministerios
Metal Slug style - parallax layers, characters prominent.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import random
import math

random.seed(42)

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "preview-sideview.png")

# Viewport: 480x270 logical, render at 3x = 1440x810
SCALE = 3
VW, VH = 480, 270
W, H = VW * SCALE, VH * SCALE

canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
draw = ImageDraw.Draw(canvas)

def load_sprite(filename, scale=SCALE):
    """Load and scale a sprite"""
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"  [SKIP] {filename} not found")
        return None
    img = Image.open(path).convert("RGBA")
    return img.resize((img.width * scale, img.height * scale), Image.NEAREST)

# ============================================================
# LAYER 0: Sky gradient (apocalyptic permanent 3PM)
# ============================================================
horizon_y = int(H * 0.44)  # horizon at 44% from top

for y in range(horizon_y + 50):
    t = y / (horizon_y + 50)
    if t < 0.3:
        # Top: Dead Night
        tt = t / 0.3
        r = int(45 * (1 - tt) + 100 * tt)
        g = int(10 * (1 - tt) + 10 * tt)
        b = int(10 * (1 - tt) + 5 * tt)
    elif t < 0.65:
        # Mid: Burnt Red
        tt = (t - 0.3) / 0.35
        r = int(100 * (1 - tt) + 180 * tt)
        g = int(10 * (1 - tt) + 40 * tt)
        b = int(5 * (1 - tt) + 10 * tt)
    else:
        # Bottom: Blood Orange near horizon
        tt = (t - 0.65) / 0.35
        r = int(180 * (1 - tt) + 255 * tt)
        g = int(40 * (1 - tt) + 107 * tt)
        b = int(10 * (1 - tt) + 53 * tt)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# Toxic green haze near horizon
for y in range(horizon_y - 30, horizon_y + 30):
    alpha = int(25 * (1 - abs(y - horizon_y) / 30))
    draw.line([(0, y), (W, y)], fill=(74, 124, 89, alpha))

# ============================================================
# LAYER 1: Congress Nacional (scrollFactor: 0.1 - very far)
# ============================================================
congress = load_sprite("sideview-bg-congresso.png")
if congress:
    cx = (W - congress.width) // 2
    cy = horizon_y - congress.height + int(20 * SCALE)
    canvas.paste(congress, (cx, cy), congress)

    # Green glow between towers
    glow_cx = cx + congress.width // 2
    glow_cy = cy + int(congress.height * 0.4)
    for r in range(40 * SCALE, 0, -1):
        alpha = int(15 * (1 - r / (40 * SCALE)))
        draw.ellipse([glow_cx - r, glow_cy - r, glow_cx + r, glow_cy + r],
                     fill=(61, 107, 58, alpha))

# ============================================================
# LAYER 2: Distant Ministries (scrollFactor: 0.25)
# ============================================================
min_far = load_sprite("sideview-ministerio-far.png")
if min_far:
    for x_pos in [int(W * 0.08), int(W * 0.30), int(W * 0.62), int(W * 0.85)]:
        my = horizon_y - min_far.height + int(15 * SCALE)
        # Slight alpha for atmospheric perspective
        faded = min_far.copy()
        canvas.paste(faded, (x_pos, my), faded)

# ============================================================
# LAYER 3: Close Ministries (scrollFactor: 0.5)
# ============================================================
min_close = load_sprite("sideview-ministerio-close.png")
if min_close:
    for x_pos in [int(W * 0.02), int(W * 0.75)]:
        my = horizon_y - min_close.height + int(35 * SCALE)
        canvas.paste(min_close, (x_pos, my), min_close)

# ============================================================
# LAYER 4: Near background objects (scrollFactor: 0.75)
# ============================================================
ground_y = horizon_y + int(10 * SCALE)  # where ground plane starts

# Trees
tree = load_sprite("sideview-arvore-seca.png")
if tree:
    for tx in [int(W * 0.15), int(W * 0.45), int(W * 0.72), int(W * 0.92)]:
        ty = ground_y - tree.height + int(8 * SCALE)
        canvas.paste(tree, (tx, ty), tree)

# Fallen lamp post
poste = load_sprite("sideview-poste-tombado.png")
if poste:
    canvas.paste(poste, (int(W * 0.55), ground_y - poste.height + int(5 * SCALE)), poste)

# Campaign signs
placa = load_sprite("sideview-placa-campanha.png")
if placa:
    for px in [int(W * 0.22), int(W * 0.65)]:
        canvas.paste(placa, (px, ground_y - placa.height + int(3 * SCALE)), placa)

# ============================================================
# LAYER 5: Ground / Road (scrollFactor: 1.0)
# ============================================================
# Draw the main ground area
ground_color = (58, 53, 48, 255)  # asphalt #3A3530
for y in range(ground_y, H):
    # Gradient from road to dirt
    t = (y - ground_y) / (H - ground_y)
    if t < 0.3:
        # Road surface
        r, g, b = 58, 53, 48
    elif t < 0.5:
        # Sidewalk
        r, g, b = 138, 133, 128
    else:
        # Dirt/grass
        tt = (t - 0.5) / 0.5
        r = int(138 * (1 - tt) + 196 * tt)
        g = int(133 * (1 - tt) + 162 * tt)
        b = int(128 * (1 - tt) + 101 * tt)
    # Add noise
    nr = max(0, min(255, r + random.randint(-8, 8)))
    ng = max(0, min(255, g + random.randint(-8, 8)))
    nb = max(0, min(255, b + random.randint(-8, 8)))
    draw.line([(0, y), (W, y)], fill=(nr, ng, nb, 255))

# Yellow road line
line_y = ground_y + int(12 * SCALE)
draw.line([(0, line_y), (W, line_y)], fill=(184, 160, 48, 150), width=max(2, SCALE))

# Road cracks
for _ in range(20):
    cx = random.randint(0, W)
    cy = ground_y + random.randint(0, int(25 * SCALE))
    cl = random.randint(5 * SCALE, 20 * SCALE)
    angle = random.uniform(-0.5, 0.5)
    ex = cx + int(cl * math.cos(angle))
    ey = cy + int(cl * math.sin(angle))
    draw.line([(cx, cy), (ex, ey)], fill=(30, 28, 25, 180), width=1)

# Scattered leaflets on ground
for _ in range(15):
    lx = random.randint(0, W)
    ly = ground_y + random.randint(int(5 * SCALE), int(40 * SCALE))
    lw = random.randint(2 * SCALE, 4 * SCALE)
    lh = random.randint(3 * SCALE, 5 * SCALE)
    draw.rectangle([lx, ly, lx + lw, ly + lh], fill=(240, 232, 208, random.randint(100, 180)))

# Blood ink stains
for _ in range(6):
    bx = random.randint(0, W)
    by = ground_y + random.randint(int(3 * SCALE), int(30 * SCALE))
    bs = random.randint(3 * SCALE, 8 * SCALE)
    draw.ellipse([bx, by, bx + bs, by + int(bs * 0.4)],
                 fill=(139, 26, 26, random.randint(60, 120)))

# ============================================================
# LAYER 5.5: Interactive objects on ground plane
# ============================================================
# Abandoned car
carro = load_sprite("sideview-carro-abandonado.png")
if carro:
    canvas.paste(carro, (int(W * 0.35), ground_y - carro.height + int(15 * SCALE)), carro)

# Barricade
barricada = load_sprite("sideview-barricada.png")
if barricada:
    canvas.paste(barricada, (int(W * 0.82), ground_y - barricada.height + int(12 * SCALE)), barricada)

# Ambulance SUS
ambulancia = load_sprite("sideview-ambulancia-sus.png")
if ambulancia:
    canvas.paste(ambulancia, (int(W * 0.05), ground_y - ambulancia.height + int(18 * SCALE)), ambulancia)

# Hot Dog cart
hotdog = load_sprite("sideview-barraca-hotdog.png")
if hotdog:
    canvas.paste(hotdog, (int(W * 0.58), ground_y - hotdog.height + int(10 * SCALE)), hotdog)

# ============================================================
# LAYER 6: Characters (placeholder silhouettes for scale)
# ============================================================
# Draw placeholder characters to show scale (48px at SCALE)
char_h = 48 * SCALE
char_w = 24 * SCALE
char_ground = ground_y + int(5 * SCALE)  # feet on ground

# Player (center) - green-ish (alive)
px = int(W * 0.48)
py = char_ground - char_h
draw.rectangle([px, py, px + char_w, char_ground],
               fill=(212, 165, 116, 220), outline=(10, 10, 10, 255), width=2)
# Head
draw.ellipse([px + 2, py - int(12 * SCALE), px + char_w - 2, py + int(4 * SCALE)],
             fill=(212, 165, 116, 220), outline=(10, 10, 10, 255), width=2)
# Weapon (broom/chinelo)
draw.line([px + char_w, py + int(10 * SCALE), px + char_w + int(20 * SCALE), py - int(5 * SCALE)],
          fill=(107, 68, 35, 255), width=max(2, SCALE))

# Zombies (left and right)
zombie_positions = [
    (int(W * 0.18), (125, 138, 106)),   # zombie left
    (int(W * 0.28), (90, 107, 74)),     # zombie left 2
    (int(W * 0.68), (125, 138, 106)),   # zombie right
    (int(W * 0.78), (90, 107, 74)),     # zombie right 2
]
for zx, zcolor in zombie_positions:
    zy = char_ground - int(44 * SCALE)
    zw = int(26 * SCALE)
    draw.rectangle([zx, zy, zx + zw, char_ground],
                   fill=(*zcolor, 200), outline=(10, 10, 10, 255), width=2)
    # Zombie head (larger, grotesque)
    draw.ellipse([zx - 2, zy - int(14 * SCALE), zx + zw + 2, zy + int(5 * SCALE)],
                 fill=(*zcolor, 200), outline=(10, 10, 10, 255), width=2)
    # Outstretched arms
    arm_dir = 1 if zx < W // 2 else -1
    draw.line([zx + zw // 2, zy + int(8 * SCALE),
               zx + zw // 2 + arm_dir * int(15 * SCALE), zy + int(5 * SCALE)],
              fill=(10, 10, 10, 200), width=max(2, SCALE - 1))

# ============================================================
# LAYER 7: Atmospheric particles (green gas + leaflets)
# ============================================================
# Green toxic gas
for _ in range(30):
    gx = random.randint(0, W)
    gy = random.randint(int(H * 0.2), int(H * 0.75))
    gs = random.randint(8 * SCALE, 20 * SCALE)
    ga = random.randint(10, 40)
    draw.ellipse([gx, gy, gx + gs, gy + int(gs * 0.6)], fill=(74, 124, 89, ga))

# Flying leaflets
for _ in range(12):
    lx = random.randint(0, W)
    ly = random.randint(int(H * 0.3), int(H * 0.8))
    lw = random.randint(3 * SCALE, 6 * SCALE)
    lh = random.randint(4 * SCALE, 7 * SCALE)
    la = random.randint(80, 180)
    angle = random.randint(-30, 30)
    draw.rectangle([lx, ly, lx + lw, ly + lh], fill=(240, 232, 208, la))

# ============================================================
# LABELS
# ============================================================
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
    font_big = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
    font_sm = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 11)
except:
    font = ImageFont.load_default()
    font_big = font
    font_sm = font

# Title
draw.text((12, 10), "ZUMBIS DE BRASILIA — Side-View Preview (Metal Slug Style)",
          fill=(240, 232, 216, 255), font=font_big)
draw.text((12, 36), "Viewport 480x270 @ 3x | Personagens 48px | Parallax 7 layers",
          fill=(240, 232, 216, 150), font=font)

# Layer labels (right side)
labels = [
    (int(H * 0.06), "Layer 0: Ceu", (200, 100, 50)),
    (int(H * 0.25), "Layer 1: Congresso (0.1x)", (61, 107, 58)),
    (int(H * 0.35), "Layer 2-3: Ministerios (0.25-0.5x)", (138, 133, 128)),
    (int(H * 0.48), "Layer 4: Objetos fundo (0.75x)", (160, 140, 100)),
    (int(H * 0.58), "Layer 5: Chao + Acao (1.0x)", (240, 200, 48)),
    (int(H * 0.72), "Layer 6: Personagens", (200, 48, 48)),
]
for ly, text, color in labels:
    draw.text((W - 320, ly), text, fill=(*color, 200), font=font_sm)

# Player label
draw.text((int(W * 0.48) - 10, char_ground + 5), "PLAYER (48px)",
          fill=(240, 200, 48, 220), font=font_sm)

# Scale indicator
draw.text((int(W * 0.18), char_ground + 5), "ZUMBI",
          fill=(125, 138, 106, 200), font=font_sm)

# ============================================================
# Save
# ============================================================
final = Image.new("RGB", canvas.size, (0, 0, 0))
final.paste(canvas, mask=canvas.split()[3])
final.save(OUT, "PNG", optimize=True)
print(f"Preview saved: {OUT}")
print(f"Size: {os.path.getsize(OUT)} bytes")
print(f"Dimensions: {final.width}x{final.height}")
