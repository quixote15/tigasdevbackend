#!/usr/bin/env python3
"""
Build a preview scene of the Esplanada dos Ministerios map
using all generated PixelLab assets.
"""

from PIL import Image, ImageDraw, ImageFont
import json
import os
import random

random.seed(42)

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "preview-esplanada.png")

# Scene dimensions (4x scale for visibility)
TILE = 16
SCALE = 3
W, H = 960, 640  # map pixel size
SW, SH = W * SCALE, H * SCALE  # scaled

canvas = Image.new("RGBA", (SW, SH), (0, 0, 0, 255))
draw = ImageDraw.Draw(canvas)

# ============================================================
# LAYER 0: Sky gradient (Blood Orange -> Burnt Red -> Dead Night)
# ============================================================
for y in range(SH):
    t = y / SH
    if t < 0.45:
        # top: Dead Night -> Burnt Red
        tt = t / 0.45
        r = int(45 * (1 - tt) + 139 * tt)
        g = int(10 * (1 - tt) + 0 * tt)
        b = int(10 * (1 - tt) + 0 * tt)
    else:
        # bottom: Burnt Red -> Blood Orange
        tt = (t - 0.45) / 0.55
        r = int(139 * (1 - tt) + 255 * tt)
        g = int(0 * (1 - tt) + 107 * tt)
        b = int(0 * (1 - tt) + 53 * tt)
    draw.line([(0, y), (SW, y)], fill=(r, g, b, 255))

# Only draw sky on top 25% (rest will be ground)
ground_start_y = int(SH * 0.18)

# ============================================================
# LAYER 1: Congress Background (parallax)
# ============================================================
congress = Image.open(os.path.join(BASE, "bg-congresso-nacional.png")).convert("RGBA")
congress_scaled = congress.resize((congress.width * SCALE, congress.height * SCALE), Image.NEAREST)
cx = (SW - congress_scaled.width) // 2
cy = ground_start_y - congress_scaled.height + 20 * SCALE
canvas.paste(congress_scaled, (cx, cy), congress_scaled)

# ============================================================
# LAYER 2: Ground tiles
# ============================================================

# Load tilesets
def load_tileset(name):
    img = Image.open(os.path.join(BASE, f"{name}.png")).convert("RGBA")
    tiles = []
    for row in range(4):
        for col in range(4):
            tile = img.crop((col * TILE, row * TILE, (col + 1) * TILE, (row + 1) * TILE))
            tiles.append(tile)
    return tiles

ts_conc_grass = load_tileset("01-concreto-grama")
ts_conc_asphalt = load_tileset("02-concreto-asfalto")
ts_conc_water = load_tileset("03-concreto-agua")
ts_grass_asphalt = load_tileset("04-grama-asfalto")
ts_var_piso = load_tileset("variantes-piso")
ts_var_overlay = load_tileset("variantes-overlay")

# Get specific terrain tiles (index 0 = full lower, 15 = full upper typically)
# From Wang tilesets: tile with all corners same = pure terrain
concrete_tile = ts_conc_grass[0]   # full concrete (lower)
grass_tile = ts_conc_grass[15]      # full grass (upper)
asphalt_tile = ts_conc_asphalt[0]   # full asphalt (lower)
water_tile = ts_conc_water[0]       # full water (lower)

# Transition tiles
conc_grass_trans = [ts_conc_grass[i] for i in [3, 5, 7, 9, 11, 13]]
conc_water_trans = [ts_conc_water[i] for i in [3, 5, 7, 9, 11, 13]]
conc_asph_trans = [ts_conc_asphalt[i] for i in [3, 5, 7, 9]]

# Map grid (60x40 tiles)
COLS, ROWS = 60, 40

# Define terrain zones
def get_terrain(col, row):
    """Return which terrain type for each tile position"""
    # Top rows 0-1: grass (north edge)
    if row < 2:
        return "grass"
    # Rows 2-5: ministry zone (mix grass + concrete)
    if 2 <= row < 6:
        # Ministry blocks at specific columns
        for mx in [8, 17, 26, 35, 44]:
            if mx <= col <= mx + 2:
                return "ministry"
        if row >= 4:
            return "concrete"
        return "grass"
    # Rows 6-11: concrete esplanade
    if 6 <= row < 12:
        return "concrete"
    # Rows 12-18: Eixo Monumental (asphalt)
    if 12 <= row < 19:
        if row in [14, 15, 16]:
            return "asphalt"
        return "concrete"
    # Rows 19-21: concrete
    if 19 <= row < 22:
        return "concrete"
    # Rows 22-26: Espelho D'Agua
    if 22 <= row < 27:
        if 14 <= col <= 45:
            return "water"
        return "concrete"
    # Rows 27-30: concrete + grass mix
    if 27 <= row < 31:
        if col < 5 or col > 54:
            return "grass"
        return "concrete"
    # Rows 31-40: south zone (grass + landmarks)
    if row >= 31:
        if col < 4 or col > 55:
            return "grass"
        if row >= 36:
            return "grass"
        return "concrete"
    return "grass"

# Draw ground layer
for row in range(ROWS):
    for col in range(COLS):
        terrain = get_terrain(col, row)
        px = col * TILE * SCALE
        py = ground_start_y + row * TILE * SCALE

        if terrain == "grass":
            tile = grass_tile
            # Random variant
            if random.random() < 0.08:
                tile = random.choice(ts_var_piso[8:12])  # grass variants
        elif terrain == "concrete":
            tile = concrete_tile
            if random.random() < 0.06:
                tile = random.choice(ts_var_piso[0:4])  # concrete variants
            if random.random() < 0.04:
                tile = random.choice(ts_var_overlay[:4])
        elif terrain == "asphalt":
            tile = asphalt_tile
            if random.random() < 0.1:
                tile = random.choice(ts_var_piso[12:16])  # asphalt variants
        elif terrain == "water":
            tile = water_tile
        elif terrain == "ministry":
            tile = concrete_tile
        else:
            tile = grass_tile

        # Scale and paste
        scaled_tile = tile.resize((TILE * SCALE, TILE * SCALE), Image.NEAREST)
        canvas.paste(scaled_tile, (px, py), scaled_tile)

# Draw transitions around water
for row in range(ROWS):
    for col in range(COLS):
        t = get_terrain(col, row)
        # Water edges
        if t == "water":
            for dc, dr in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nc, nr = col + dc, row + dr
                if 0 <= nc < COLS and 0 <= nr < ROWS:
                    nt = get_terrain(nc, nr)
                    if nt != "water":
                        px = nc * TILE * SCALE
                        py = ground_start_y + nr * TILE * SCALE
                        trans = random.choice(conc_water_trans)
                        st = trans.resize((TILE * SCALE, TILE * SCALE), Image.NEAREST)
                        canvas.paste(st, (px, py), st)

# Asphalt yellow line
for col in range(COLS):
    for row_off in [15]:
        px = col * TILE * SCALE
        py = ground_start_y + row_off * TILE * SCALE
        # Draw faded yellow line
        line_y = py + (TILE * SCALE) // 2
        draw.line([(px, line_y), (px + TILE * SCALE, line_y)], fill=(184, 160, 48, 180), width=max(1, SCALE))

# ============================================================
# LAYER 3: Buildings (Ministries)
# ============================================================
ministerio = Image.open(os.path.join(BASE, "building-ministerio-normal.png")).convert("RGBA")
min_scaled = ministerio.resize((ministerio.width * SCALE, ministerio.height * SCALE), Image.NEAREST)

placas = []
for i in range(1, 6):
    try:
        p = Image.open(os.path.join(BASE, f"placa-m{i}-{'enrolacao' if i==1 else 'puxadinho' if i==2 else 'promessa' if i==3 else 'jeitinho' if i==4 else 'planilha'}.png")).convert("RGBA")
        placas.append(p.resize((p.width * SCALE, p.height * SCALE), Image.NEAREST))
    except:
        placas.append(None)

ministry_positions = [8, 17, 26, 35, 44]
for idx, mx in enumerate(ministry_positions):
    px = mx * TILE * SCALE
    py = ground_start_y + 1 * TILE * SCALE
    canvas.paste(min_scaled, (px, py), min_scaled)
    # Plaque below
    if idx < len(placas) and placas[idx]:
        placa = placas[idx]
        ppx = px + (min_scaled.width - placa.width) // 2
        ppy = py + min_scaled.height - 5 * SCALE
        canvas.paste(placa, (ppx, ppy), placa)

# ============================================================
# LAYER 4: Landmarks
# ============================================================
def place_sprite(filename, tile_x, tile_y):
    try:
        img = Image.open(os.path.join(BASE, filename)).convert("RGBA")
        scaled = img.resize((img.width * SCALE, img.height * SCALE), Image.NEAREST)
        px = tile_x * TILE * SCALE
        py = ground_start_y + tile_y * TILE * SCALE
        canvas.paste(scaled, (px, py), scaled)
    except Exception as e:
        print(f"Warning: could not place {filename}: {e}")

place_sprite("landmark-helicoptero-ibama.png", 16, 30)
place_sprite("landmark-cabine-votacao.png", 25, 31)
place_sprite("landmark-ambulancia-sus.png", 31, 31)
place_sprite("landmark-buffet-abandonado.png", 38, 30)
place_sprite("landmark-palanque-eleitoral.png", 27, 35)
place_sprite("landmark-barraca-hotdog.png", 21, 34)

# ============================================================
# LAYER 5: Decorations (scattered)
# ============================================================
deco_files = [
    "deco-poste-caido.png",
    "deco-placa-campanha.png",
    "deco-banco-quebrado.png",
    "deco-lixeira.png",
    "deco-cone-transito.png",
    "deco-barricada.png",
    "deco-aspersor-quebrado.png",
    "deco-carro-abandonado.png",
    "deco-pneus.png",
    "deco-fogueira.png",
]

# Place decorations at semi-random positions
deco_positions = [
    (5, 8), (12, 10), (50, 7), (42, 9),    # concrete zone
    (3, 33), (52, 35), (8, 37), (55, 38),   # grass zone south
    (20, 13), (40, 13),                       # near eixo
    (10, 28), (48, 29),                       # south of water
    (15, 20), (45, 20),                       # between eixo and water
]

for i, (dx, dy) in enumerate(deco_positions):
    deco_file = deco_files[i % len(deco_files)]
    place_sprite(deco_file, dx, dy)

# ============================================================
# LAYER 6: Ambient particles (static representation)
# ============================================================
# Green gas particles near congress/water
for _ in range(40):
    gx = random.randint(int(SW * 0.2), int(SW * 0.8))
    gy = ground_start_y + random.randint(0, int(ROWS * TILE * SCALE * 0.5))
    size = random.randint(4 * SCALE, 10 * SCALE)
    alpha = random.randint(20, 60)
    draw.ellipse([gx, gy, gx + size, gy + size], fill=(74, 124, 89, alpha))

# Electoral leaflets floating
for _ in range(25):
    lx = random.randint(0, SW)
    ly = ground_start_y + random.randint(0, int(ROWS * TILE * SCALE))
    lw, lh = random.randint(3 * SCALE, 5 * SCALE), random.randint(4 * SCALE, 6 * SCALE)
    rot = random.randint(0, 360)
    alpha = random.randint(120, 200)
    draw.rectangle([lx, ly, lx + lw, ly + lh], fill=(240, 232, 208, alpha))

# ============================================================
# LAYER 7: Labels for the preview
# ============================================================
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
    font_big = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 11)
except:
    font = ImageFont.load_default()
    font_big = font
    font_small = font

# Title
draw.text((10, 10), "ZUMBIS DE BRASILIA — Esplanada dos Ministerios (MVP Preview)", fill=(240, 232, 216, 255), font=font_big)
draw.text((10, 40), "Todos os assets gerados via PixelLab MCP — Estilo Andre Guedes", fill=(240, 232, 216, 180), font=font)

# Zone labels
label_y_base = ground_start_y
draw.text((10, label_y_base + 2 * TILE * SCALE), "← MINISTERIOS (M1-M5)", fill=(240, 200, 48, 200), font=font_small)
draw.text((10, label_y_base + 14 * TILE * SCALE), "← EIXO MONUMENTAL", fill=(240, 200, 48, 200), font=font_small)
draw.text((10, label_y_base + 23 * TILE * SCALE), "← ESPELHO D'AGUA (kill zone)", fill=(61, 107, 58, 220), font=font_small)
draw.text((10, label_y_base + 32 * TILE * SCALE), "← LANDMARKS / ZONA DE COMBATE", fill=(240, 200, 48, 200), font=font_small)
draw.text((10, label_y_base + 37 * TILE * SCALE), "← SPAWN DO JOGADOR", fill=(200, 48, 48, 220), font=font_small)

# Player spawn indicator
spawn_x = 30 * TILE * SCALE
spawn_y = ground_start_y + 38 * TILE * SCALE
draw.ellipse([spawn_x - 8, spawn_y - 8, spawn_x + 8, spawn_y + 8], fill=(200, 48, 48, 200))
draw.text((spawn_x + 12, spawn_y - 6), "PLAYER", fill=(200, 48, 48, 220), font=font_small)

# ============================================================
# Save
# ============================================================
# Convert to RGB for smaller file
final = Image.new("RGB", canvas.size, (0, 0, 0))
final.paste(canvas, mask=canvas.split()[3])
final.save(OUT, "PNG", optimize=True)

print(f"Preview saved: {OUT}")
print(f"Size: {os.path.getsize(OUT)} bytes")
print(f"Dimensions: {final.width}x{final.height}")
