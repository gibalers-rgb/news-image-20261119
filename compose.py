#!/usr/bin/env python3
"""Compose the 19 Nov 2026 world-news summary image (1024x1024 PNG)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (16, 24, 64)
GOLD = (201, 162, 39)
TEAL = (0, 128, 128)
PAPER = (247, 243, 234)
INK = (18, 22, 40)
MUTED = (90, 92, 110)
RED = (178, 34, 34)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(p, s):
    return ImageFont.truetype(p, s)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- header band ----
d.rectangle([0, 0, W, 118], fill=NAVY)
d.rectangle([0, 118, W, 122], fill=GOLD)
d.text((32, 16), "THE WORLD  •  IN ONE PAGE", font=font(SANS_B, 22), fill=GOLD)
d.text((32, 46), "THURSDAY, 19 NOVEMBER 2026", font=font(SERIF_B, 44), fill=(255, 255, 255))

# ---- AI banner (cover-resize to 1024x268) ----
banner = Image.open("assets/media-generation-news-banner-20261119-0-47fdd768-e7f8-4221-bf49-a3c6e2e90b3a.png").convert("RGB")
bw, bh = banner.size
target_h = 268
scale = max(W / bw, target_h / bh)
banner = banner.resize((int(bw * scale), int(bh * scale)))
bx = (banner.width - W) // 2
by = (banner.height - target_h) // 2
img.paste(banner.crop((bx, by, bx + W, by + target_h)), (0, 122))
d.rectangle([0, 122 + target_h, W, 122 + target_h + 4], fill=GOLD)

# ---- story panels: 2 cols x 3 rows ----
stories = [
    ("SUMMIT  •  SHENZHEN", "Trump, Xi & Putin meet",
     "First-ever trilateral summit ends with a four-point \u201cDeclaration toward Peace\u201d and a pledge to cut nuclear risks.", TEAL),
    ("JUSTICE  •  THE HAGUE", "Myanmar guilty of genocide",
     "The world court rules 9\u20136: Myanmar\u2019s military committed genocide against the Rohingya in 2017.", RED),
    ("MARKETS  •  NEW YORK", "Anthropic\u2019s record debut",
     "Priced at $83 and valued near $1.5 trillion, the AI firm\u2019s shares jump about 34% on day one.", NAVY),
    ("GAZA", "Peace plan scores 4 out of 26",
     "Five aid groups say the Gaza plan is falling far short as the IDF\u2019s Nuseirat operation ends.", (150, 90, 0)),
    ("CLIMATE  •  ANTALYA", "COP31 draft drops fossil fuels",
     "Ministers race to unblock climate talks after fossil-fuel language is cut from the draft deal.", (0, 110, 60)),
    ("EUROPE  •  UKRAINE", "\u20ac45bn lifeline for Kyiv",
     "The EU proposes a \u20ac45bn loan; the UK pledges 1,000+ drones in a \u00a3260m package for Ukraine.", (90, 40, 120)),
]

top = 122 + target_h + 4
panel_w, panel_h = 480, 168
gap_x, gap_y = 24, 16
for i, (tag, head, body, color) in enumerate(stories):
    r, c = divmod(i, 2)
    x = 32 + c * (panel_w + gap_x)
    y = top + 14 + r * (panel_h + gap_y)
    d.rounded_rectangle([x, y, x + panel_w, y + panel_h], radius=10, outline=(200, 196, 180), width=2, fill=(255, 255, 255))
    d.rectangle([x, y, x + 8, y + panel_h], fill=color)
    d.text((x + 24, y + 12), tag, font=font(SANS_B, 17), fill=color)
    d.text((x + 24, y + 38), head, font=font(SERIF_B, 25), fill=INK)
    lines = wrap(d, body, font(SANS, 19), panel_w - 48)
    yy = y + 76
    for ln in lines[:3]:
        d.text((x + 24, yy), ln, font=font(SANS, 19), fill=MUTED)
        yy += 26

# ---- footer ----
fy = top + 14 + 3 * panel_h + 2 * gap_y + 8
d.line([32, fy, W - 32, fy], fill=(200, 196, 180), width=2)
d.text((32, fy + 10), "Sources: BBC, Le Monde, Dow Jones, AP, ICJ, APEC  •  Events of 19 November 2026, all time zones.",
       font=font(SANS, 16), fill=MUTED)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
