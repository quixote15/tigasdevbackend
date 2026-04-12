#!/usr/bin/env python3
"""
Build a panoramic preview of all 5 map segments side by side,
showing the full 9600px level progression from Ministries to Congress.
"""

from PIL import Image, ImageDraw, ImageFont
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SIDEVIEW = os.path.dirname(BASE) if os.path.basename(BASE) == "maps" else BASE
MAPS = os.path.join(SIDEVIEW, "maps") if os.path.exists(os.path.join(SIDEVIEW, "maps")) else BASE
OUT = os.path.join(MAPS, "preview-full-level.png")

# Each segment: 384px wide. 5 segments = 1920px total for preview.
# We'll show at 2x scale = 3840px, but that's too wide.
# Instead: show each segment as a 384x270 panel (full viewport height)
SEG_W = 384
VP_H = 270
SCALE = 2
PANEL_W = SEG_W * SCALE
PANEL_H = VP_H * SCALE
TOTAL_W = PANEL_W * 5
TOTAL_H = PANEL_H + 80  # extra for labels

canvas = Image.new("RGB", (TOTAL_W, TOTAL_H), (20, 10, 10))
draw = ImageDraw.Draw(canvas)

def load_img(filename):
    path = os.path.join(MAPS, filename)
    if not os.path.exists(path):
        path = os.path.join(SIDEVIEW, filename)
    if not os.path.exists(path):
        print(f"  [SKIP] {filename}")
        return None
    return Image.open(path).convert("RGBA")

def paste_scaled(img, x, y, scale=SCALE):
    """Paste image scaled with nearest neighbor"""
    if img is None:
        return
    scaled = img.resize((img.width * scale, img.height * scale), Image.NEAREST)
    # Convert to RGB-compatible paste
    canvas.paste(
        Image.composite(scaled, Image.new("RGBA", scaled.size, (0, 0, 0, 0)), scaled).convert("RGB"),
        (x, y),
    )

def draw_sky_gradient(x_start, width, y_start=0, height=None):
    """Draw the apocalyptic sky gradient"""
    if height is None:
        height = int(PANEL_H * 0.45)
    for y in range(height):
        t = y / height
        if t < 0.3:
            tt = t / 0.3
            r = int(45 * (1 - tt) + 100 * tt)
            g = int(10 * (1 - tt) + 10 * tt)
            b = int(10 * (1 - tt) + 5 * tt)
        elif t < 0.65:
            tt = (t - 0.3) / 0.35
            r = int(100 * (1 - tt) + 180 * tt)
            g = int(10 * (1 - tt) + 40 * tt)
            b = int(5 * (1 - tt) + 10 * tt)
        else:
            tt = (t - 0.65) / 0.35
            r = int(180 * (1 - tt) + 255 * tt)
            g = int(40 * (1 - tt) + 107 * tt)
            b = int(10 * (1 - tt) + 53 * tt)
        draw.line([(x_start, y_start + y), (x_start + width, y_start + y)],
                  fill=(r, g, b))

# Load all assets
sky = load_img("sky-apocalyptic-strip.png")
seg1_bg = load_img("seg1-ministerios-corridor.png")
seg1_fg = load_img("seg1-foreground-strip.png")
seg2_bg = load_img("seg2-eixo-monumental-bg.png")
seg2_fg = load_img("seg2-highway-ground.png")
seg3_bg = load_img("seg3-espelho-dagua-bg.png")
seg3_fg = load_img("seg3-water-edge-ground.png")
seg4_bg = load_img("seg4-rampa-congresso-bg.png")
seg4_fg = load_img("seg4-ramp-ground.png")
seg5_bg = load_img("seg5-plenario-interior-bg.png")
seg5_fg = load_img("seg5-plenario-ground.png")
congresso_full = load_img("congresso-full-facade.png")
congresso_sv = load_img("sideview-bg-congresso.png")

# Ground color for each segment
ground_colors = [
    (138, 133, 128),  # seg1: concrete
    (58, 53, 48),     # seg2: asphalt
    (80, 90, 75),     # seg3: green-tinged concrete
    (100, 80, 80),    # seg4: ramp/carpet
    (70, 50, 50),     # seg5: marble/carpet
]

segments = [
    ("SEG 1: MINISTERIOS", "Waves 1-3 | Corredor brutalista", seg1_bg, seg1_fg),
    ("SEG 2: EIXO MONUMENTAL", "Waves 4-7 | Rodovia aberta", seg2_bg, seg2_fg),
    ("SEG 3: ESPELHO D'AGUA", "Waves 8-11 | Kill zone agua", seg3_bg, seg3_fg),
    ("SEG 4: RAMPA CONGRESSO", "Waves 12-15 | Gas denso", seg4_bg, seg4_fg),
    ("SEG 5: PLENARIO", "Boss Final | Interior Congresso", seg5_bg, seg5_fg),
]

try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 13)
    font_big = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
except:
    font = ImageFont.load_default()
    font_big = font
    font_title = font

for i, (title, subtitle, bg, fg) in enumerate(segments):
    x = i * PANEL_W

    # Sky gradient
    if sky:
        paste_scaled(sky, x, 0)
    else:
        draw_sky_gradient(x, PANEL_W)

    # Congress in background for segments 3-5 (getting bigger)
    if i >= 2 and congresso_sv:
        cscale = [0, 0, 1.5, 2.5, 0][i]  # seg5 uses full facade instead
        if cscale > 0:
            cw = int(congresso_sv.width * SCALE * cscale)
            ch = int(congresso_sv.height * SCALE * cscale)
            cs = congresso_sv.resize((cw, ch), Image.NEAREST)
            cx = x + (PANEL_W - cw) // 2
            cy = int(PANEL_H * 0.25) - ch // 2
            try:
                canvas.paste(Image.composite(cs, Image.new("RGBA", cs.size, (0,0,0,0)), cs).convert("RGB"), (cx, max(0, cy)))
            except:
                pass

    # Segment 5: Congress full facade
    if i == 4 and congresso_full:
        paste_scaled(congresso_full, x + (PANEL_W - congresso_full.width * SCALE) // 2, int(PANEL_H * 0.05))

    # Background strip
    if bg:
        bg_y = int(PANEL_H * 0.25)
        paste_scaled(bg, x, bg_y)

    # Ground fill
    ground_y = int(PANEL_H * 0.85)
    gc = ground_colors[i]
    draw.rectangle([x, ground_y, x + PANEL_W, PANEL_H], fill=gc)

    # Foreground strip on ground
    if fg:
        fg_y = ground_y - fg.height * SCALE + int(10 * SCALE)
        paste_scaled(fg, x, fg_y)

    # Segment divider line
    if i > 0:
        draw.line([(x, 0), (x, PANEL_H)], fill=(255, 200, 48, 200), width=2)

    # Labels at bottom
    label_y = PANEL_H + 8
    draw.text((x + 10, label_y), title, fill=(240, 200, 48), font=font_big)
    draw.text((x + 10, label_y + 22), subtitle, fill=(200, 180, 150), font=font)

    # Segment number
    draw.text((x + PANEL_W - 30, 10), f"S{i+1}", fill=(255, 200, 48, 150), font=font_big)

# Title bar
draw.text((10, PANEL_H + 52),
          "ZUMBIS DE BRASILIA — Mapa Completo Side-View (9600px = 5 segmentos) | Estilo Metal Slug | Andre Guedes Art Direction",
          fill=(240, 232, 216, 200), font=font)

# Direction arrow
arrow_y = PANEL_H + 52
draw.text((TOTAL_W - 200, PANEL_H + 8), "DIRECAO →", fill=(240, 200, 48), font=font_big)
draw.text((TOTAL_W - 200, PANEL_H + 30), "Jogador avanca →", fill=(200, 180, 150), font=font)
draw.text((TOTAL_W - 200, PANEL_H + 48), "rumo ao Congresso", fill=(200, 180, 150), font=font)

canvas.save(OUT, "PNG", optimize=True)
print(f"Preview saved: {OUT}")
print(f"Size: {os.path.getsize(OUT)} bytes")
print(f"Dimensions: {canvas.width}x{canvas.height}")
