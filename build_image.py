"""Draw the entry image for make.fun news-image-20261120.

A one-page newspaper front page for Friday 20 November 2026: six verified
stories of the day, drawn with Pillow only. Deterministic output: the same
bytes every run. Run:  python3 build_image.py  ->  entry.png (1024x1024)
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

PAPER = (246, 241, 231)
NAVY = (22, 35, 63)
GOLD = (217, 164, 65)
INK = (24, 24, 24)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
BORDER = (216, 210, 196)

STORIES = [
    {
        "kicker": "SHENZHEN  ·  SUMMIT",
        "color": (15, 118, 110),
        "icon": "summit",
        "headline": "Trump, Xi and Putin hold first three-way summit",
        "detail": "Leaders sign a four-point peace declaration after 70 minutes of talks.",
    },
    {
        "kicker": "THE HAGUE  ·  JUSTICE",
        "color": (109, 40, 217),
        "icon": "scales",
        "headline": "World Court: Myanmar guilty of Rohingya genocide",
        "detail": "9\u20136 ruling, the first time the court has held a state responsible for genocide.",
    },
    {
        "kicker": "CRIMEA  ·  WAR",
        "color": (185, 28, 28),
        "icon": "bridge",
        "headline": "Ukraine hits Crimea Bridge a third time",
        "detail": "Rail halted; Putin vows a \u201cfar more painful\u201d reply as Kyiv is struck again.",
    },
    {
        "kicker": "NEW YORK  ·  MARKETS",
        "color": (21, 128, 61),
        "icon": "chart_up",
        "headline": "Anthropic jumps 17% in Nasdaq debut",
        "detail": "Shares close near $97 after a record $81.3bn IPO valuing the firm at $1.5tn.",
    },
    {
        "kicker": "RIYADH  ·  MIDDLE EAST",
        "color": (180, 83, 9),
        "icon": "tower",
        "headline": "Houthi missile damages Riyadh finance tower",
        "detail": "Sovereign wealth fund tower hit, no injuries; a tanker burns in Hormuz after a mine strike.",
    },
    {
        "kicker": "GLOBAL MARKETS  ·  ECONOMY",
        "color": (29, 78, 216),
        "icon": "chart_down",
        "headline": "Stocks fall for a fifth straight day",
        "detail": "S&P 500 \u22122%, Nikkei \u22124.8%, SoftBank \u221216%; gold \u22124.2% as Brent holds $90.",
    },
]


def wrap(draw, text, font, width):
    """Wrap text to fit width in pixels, returning a list of lines."""
    words = text.split()
    lines, line = [], ""
    for word in words:
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_icon(draw, kind, cx, cy, color):
    """A small flat pictogram, centred on (cx, cy), inside a 64px box."""
    s = 30
    if kind == "summit":
        for dx in (-22, 0, 22):
            draw.line([cx + dx, cy - 26, cx + dx, cy + 26], fill=color, width=4)
            draw.polygon([(cx + dx, cy - 26), (cx + dx + 16, cy - 20), (cx + dx, cy - 14)],
                         fill=color)
    elif kind == "scales":
        draw.line([cx, cy - 26, cx, cy + 26], fill=color, width=4)
        draw.line([cx - 26, cy - 18, cx + 26, cy - 18], fill=color, width=4)
        draw.line([cx - 26, cy - 18, cx - 34, cy + 2], fill=color, width=3)
        draw.line([cx - 26, cy - 18, cx - 18, cy + 2], fill=color, width=3)
        draw.line([cx + 26, cy - 18, cx + 18, cy + 2], fill=color, width=3)
        draw.line([cx + 26, cy - 18, cx + 34, cy + 2], fill=color, width=3)
        draw.arc([cx - 36, cy - 4, cx - 16, cy + 16], 0, 180, fill=color, width=3)
        draw.arc([cx + 16, cy - 4, cx + 36, cy + 16], 0, 180, fill=color, width=3)
    elif kind == "bridge":
        draw.arc([cx - 30, cy - 20, cx + 30, cy + 28], 180, 360, fill=color, width=4)
        draw.line([cx - 32, cy + 4, cx + 32, cy + 4], fill=color, width=4)
        for dx in (-20, 0, 20):
            draw.line([cx + dx, cy - 8, cx + dx, cy + 4], fill=color, width=3)
    elif kind == "chart_up":
        for i, h in enumerate((14, 24, 34)):
            x0 = cx - 28 + i * 20
            draw.rectangle([x0, cy + 18 - h, x0 + 12, cy + 18], fill=color)
        draw.line([cx - 30, cy - 22, cx - 8, cy - 2, cx + 8, cy - 12, cx + 30, cy - 26],
                  fill=color, width=4)
        draw.polygon([(cx + 30, cy - 26), (cx + 18, cy - 26), (cx + 30, cy - 14)], fill=color)
    elif kind == "chart_down":
        for i, h in enumerate((34, 24, 14)):
            x0 = cx - 28 + i * 20
            draw.rectangle([x0, cy + 18 - h, x0 + 12, cy + 18], fill=color)
        draw.line([cx - 30, cy - 26, cx - 8, cy - 12, cx + 8, cy - 2, cx + 30, cy - 22],
                  fill=color, width=4)
        draw.polygon([(cx + 30, cy - 22), (cx + 18, cy - 22), (cx + 30, cy - 10)], fill=color)
    elif kind == "tower":
        draw.rectangle([cx - 12, cy - 24, cx + 12, cy + 26], fill=color)
        draw.polygon([(cx - 12, cy - 24), (cx + 12, cy - 24), (cx, cy - 34)], fill=color)
        for yy in (-12, 0, 12):
            draw.rectangle([cx - 6, cy + yy, cx + 6, cy + yy + 5], fill=PAPER)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    f_kicker = ImageFont.truetype(FONTB, 19)
    f_head = ImageFont.truetype(FONTB, 29)
    f_detail = ImageFont.truetype(FONT, 21)
    f_mast_small = ImageFont.truetype(FONTB, 25)
    f_mast_big = ImageFont.truetype(FONTB, 58)
    f_mast_sub = ImageFont.truetype(FONT, 26)
    f_foot = ImageFont.truetype(FONT, 17)

    # Masthead
    draw.rounded_rectangle([28, 26, W - 28, 178], radius=10, fill=NAVY)
    draw.text((56, 44), "T H E   W O R L D   I N   O N E   P A G E", font=f_mast_small, fill=GOLD)
    draw.text((54, 76), "FRIDAY 20 NOVEMBER 2026", font=f_mast_big, fill=(255, 255, 255))
    draw.text((56, 142), "Six stories that defined the day", font=f_mast_sub, fill=(200, 205, 220))

    # Story cards: 2 columns x 3 rows
    x0, y0 = 28, 196
    cw, ch, gap = 472, 237, 16
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = x0 + col * (cw + gap)
        y = y0 + row * (ch + gap)
        color = story["color"]
        draw.rounded_rectangle([x, y, x + cw, y + ch], radius=8, fill=CARD,
                               outline=BORDER, width=2)
        draw.rounded_rectangle([x, y, x + cw, y + 8], radius=4, fill=color)
        draw.rectangle([x, y + 4, x + cw, y + 8], fill=color)
        tx = x + 18
        text_w = cw - 18 - 96
        draw.text((tx, y + 22), story["kicker"], font=f_kicker, fill=color)
        draw_icon(draw, story["icon"], x + cw - 52, y + 62, color)
        lines = wrap(draw, story["headline"], f_head, text_w)[:3]
        ly = y + 52
        for line in lines:
            draw.text((tx, ly), line, font=f_head, fill=INK)
            ly += 34
        dlines = wrap(draw, story["detail"], f_detail, text_w + 78)[:3]
        ly += 6
        for line in dlines:
            draw.text((tx, ly), line, font=f_detail, fill=GREY)
            ly += 27

    # Footer
    draw.rounded_rectangle([28, 952, W - 28, 994], radius=8, fill=NAVY)
    foot = "20 NOVEMBER 2026  ·  EVENTS REPORTED ON 20 NOV 2026  ·  BBC, GUARDIAN, SKY NEWS, CNBC, AL JAZEERA"
    fw = draw.textlength(foot, font=f_foot)
    draw.text(((W - fw) / 2, 964), foot, font=f_foot, fill=(220, 225, 235))

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
