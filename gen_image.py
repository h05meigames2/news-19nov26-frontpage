#!/usr/bin/env python3
"""Render the 19 November 2026 front page as entry.png (1024x1024).

Draws a newspaper front page with PIL: a masthead naming the day, then six
story panels, each with a procedurally drawn pictogram and a short factual
headline. No external images are used; every shape is drawn in code.
"""

import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 240, 224)
INK = (18, 32, 66)
RED = (178, 34, 34)
GOLD = (201, 141, 42)
TEAL = (31, 110, 110)
SKY = (120, 165, 205)
LIGHT = (255, 255, 255)
GREY = (90, 90, 90)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


F_TITLE = font("DejaVuSerif-Bold.ttf", 64)
F_DATE = font("DejaVuSans-Bold.ttf", 30)
F_HEAD = font("DejaVuSans-Bold.ttf", 25)
F_SUB = font("DejaVuSans.ttf", 19)
F_TAG = font("DejaVuSans-Bold.ttf", 17)
F_FOOT = font("DejaVuSans.ttf", 17)


def wrap(draw, text, fnt, width):
    """Wrap text into lines no wider than width pixels."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, x, y, w, h, tag, headline, sub, art):
    """One story panel: tag line, pictogram area, headline, sub-line."""
    draw.rectangle([x, y, x + w, y + h], fill=LIGHT, outline=INK, width=2)
    draw.rectangle([x, y, x + w, y + 30], fill=INK)
    draw.text((x + 10, y + 5), tag, font=F_TAG, fill=LIGHT)
    art(x, y + 30, w, 118)
    lines = wrap(draw, headline, F_HEAD, w - 20)
    ty = y + 152
    for line in lines[:3]:
        draw.text((x + 10, ty), line, font=F_HEAD, fill=INK)
        ty += 29
    draw.text((x + 10, y + h - 26), sub, font=F_SUB, fill=GREY)


def art_summit(draw, x, y, w, h):
    """Three leaders seated at a long table with three flags."""
    draw.rectangle([x, y, x + w, y + h], fill=(214, 228, 240))
    for i, col in enumerate([(178, 34, 34), (31, 110, 110), (201, 141, 42)]):
        cx = x + 90 + i * 150
        draw.rectangle([cx - 4, y + 18, cx + 4, y + 52], fill=INK)
        draw.polygon([(cx + 4, y + 18), (cx + 34, y + 26), (cx + 4, y + 34)],
                     fill=col)
        draw.ellipse([cx - 16, y + 52, cx + 16, y + 84], fill=(232, 190, 160))
        draw.rectangle([cx - 22, y + 84, cx + 22, y + 112], fill=col)
    draw.rectangle([x + 30, y + 100, x + w - 30, y + 112], fill=(120, 82, 50))


def art_strike(draw, x, y, w, h):
    """Missile arc over a radar dish and gulf coastline."""
    draw.rectangle([x, y, x + w, y + h], fill=(24, 38, 64))
    for i in range(5):
        draw.ellipse([x + 40 + i * 90, y + 12 + (i % 2) * 8,
                      x + 48 + i * 90, y + 20 + (i % 2) * 8], fill=LIGHT)
    draw.arc([x + 60, y + 2, x + 300, y + 95], 200, 340, fill=RED, width=6)
    draw.polygon([(x + 250, y + 18), (x + 262, y + 44), (x + 238, y + 44)],
                 fill=RED)
    draw.arc([x + 300, y + 40, x + 380, y + 118], 180, 270, fill=(150, 200, 150),
             width=4)
    draw.line([x + 340, y + 78, x + 380, y + 118], fill=(150, 200, 150), width=4)
    draw.rectangle([x + 30, y + 96, x + w - 30, y + 112], fill=(31, 110, 110))


def art_gta(draw, x, y, w, h):
    """Neon Vice City skyline at dusk with a palm and sun."""
    draw.rectangle([x, y, x + w, y + h], fill=(58, 28, 84))
    draw.ellipse([x + w - 120, y + 8, x + w - 40, y + 88], fill=(255, 140, 90))
    for bx, bh, col in [(40, 70, (255, 0, 128)), (110, 95, (0, 220, 255)),
                        (190, 60, (255, 220, 0)), (260, 85, (255, 0, 128)),
                        (330, 55, (0, 220, 255)), (400, 75, (255, 220, 0))]:
        draw.rectangle([x + bx, y + 112 - bh, x + bx + 55, y + 112], fill=col)
        for wy in range(y + 112 - bh + 8, y + 104, 16):
            draw.rectangle([x + bx + 8, wy, x + bx + 18, wy + 8], fill=LIGHT)
    draw.line([x + 60, y + 55, x + 60, y + 112], fill=(0, 160, 60), width=6)
    for dx, dy in [(-38, -22), (-8, -30), (24, -26), (40, -8)]:
        draw.arc([x + 60 + dx - 22, y + 55 + dy - 10, x + 60 + dx + 22,
                  y + 55 + dy + 14], 180, 360, fill=(0, 200, 80), width=4)


def art_cyclone(draw, x, y, w, h):
    """Spiral cyclone over a coastline."""
    draw.rectangle([x, y, x + w, y + h], fill=(190, 215, 235))
    cx, cy = x + w // 2 - 40, y + 58
    for turn in range(3):
        r0 = 8 + turn * 14
        pts = []
        for a in range(0, 300, 6):
            r = r0 + a * 0.09
            pts.append((cx + r * math.cos(math.radians(a + turn * 40)),
                        cy + r * math.sin(math.radians(a + turn * 40))))
        draw.line(pts, fill=TEAL if turn % 2 == 0 else INK, width=5)
    draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=RED)
    draw.rectangle([x + 30, y + 96, x + w - 30, y + 112], fill=(31, 110, 110))
    draw.text((x + w - 130, y + 6), "INDIA →", font=F_TAG, fill=INK)


def art_gavel(draw, x, y, w, h):
    """Speaker's gavel and podium with a star-spangled backdrop."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 222, 196))
    draw.rectangle([x + 60, y + 78, x + w - 60, y + 112], fill=(120, 82, 50))
    draw.rectangle([x + 180, y + 30, x + 300, y + 52], fill=(90, 60, 30))
    draw.line([x + 240, y + 52, x + 240, y + 80], fill=(90, 60, 30), width=8)
    draw.rectangle([x + 320, y + 62, x + 340, y + 74], fill=(90, 60, 30))
    for sx, sy in [(90, 30), (150, 55), (330, 35), (390, 60), (430, 30)]:
        px, py = x + sx, y + sy
        draw.polygon([(px, py - 8), (px + 3, py - 1), (px + 9, py),
                      (px + 3, py + 3), (px, py + 9), (px - 3, py + 3),
                      (px - 9, py), (px - 3, py - 1)], fill=RED)


def art_voyager(draw, x, y, w, h):
    """Voyager probe with dish and golden record, among stars."""
    draw.rectangle([x, y, x + w, y + h], fill=(12, 18, 44))
    for sx, sy in [(60, 20), (140, 45), (220, 18), (320, 40), (400, 22),
                   (90, 80), (280, 75), (380, 85), (180, 95)]:
        draw.ellipse([x + sx, y + sy, x + sx + 4, y + sy + 4], fill=LIGHT)
    draw.ellipse([x + 150, y + 40, x + 210, y + 100], fill=GOLD,
                 outline=LIGHT, width=2)
    draw.polygon([(x + 210, y + 55), (x + 260, y + 45), (x + 260, y + 85),
                  (x + 210, y + 75)], fill=(200, 200, 210))
    draw.line([x + 150, y + 70, x + 100, y + 90], fill=LIGHT, width=3)
    draw.line([x + 100, y + 90, x + 130, y + 95], fill=LIGHT, width=3)
    draw.ellipse([x + 330, y + 30, x + 360, y + 60], fill=(120, 165, 205))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=6)

    # Masthead
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=F_TITLE)
    d.text(((W - tw) / 2, 18), title, font=F_TITLE, fill=INK)
    d.line([24, 96, W - 24, 96], fill=RED, width=4)
    date = "THURSDAY, 19 NOVEMBER 2026"
    dw = d.textlength(date, font=F_DATE)
    d.text(((W - dw) / 2, 106), date, font=F_DATE, fill=RED)
    d.line([24, 148, W - 24, 148], fill=INK, width=3)

    stories = [
        ("APEC · SHENZHEN", "TRUMP–XI–PUTIN MEET IN SHENZHEN",
         "Trilateral talks open at APEC summit", art_summit),
        ("WAR · THE GULF", "IRAN HITS US BASES IN KUWAIT AND BAHRAIN",
         "US–Iran war widens after Qeshm strike", art_strike),
        ("GAMES", "GTA VI LAUNCHES — VICE CITY OPENS",
         "Global launch after a 13-year wait", art_gta),
        ("WEATHER · INDIA", "CYCLONE AKVAN NEARS INDIA'S EAST COAST",
         "Landfall feared between Machilipatnam and Puri", art_cyclone),
        ("USA · CONGRESS", "JEFFRIES SET TO BE FIRST BLACK SPEAKER",
         "Democrats nominate Hakeem Jeffries", art_gavel),
        ("SPACE", "VOYAGER 1 REACHES A LIGHT-DAY FROM EARTH",
         "NASA confirms the milestone today", art_voyager),
    ]
    gx, gy = 24, 168
    pw, ph = 478, 262
    gap = 20
    for i, (tag, head, sub, art) in enumerate(stories):
        x = gx + (i % 2) * (pw + gap)
        y = gy + (i // 2) * (ph + gap)
        draw_panel(d, x, y, pw, ph, tag, head, sub,
                   lambda dx, dy, dw, dh, a=art: a(d, dx, dy, dw, dh))

    d.text((24, 996), "Six stories that defined the day — drawn from the day's reporting.",
           font=F_FOOT, fill=GREY)
    img.save("entry.png")
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
