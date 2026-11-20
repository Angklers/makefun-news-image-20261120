#!/usr/bin/env python3
"""Build the entry image: a one-page newspaper front page for Friday
20 November 2026, with 18 verified stories from that day, across six
continents and every field (politics, justice, war, climate, disaster,
markets, tech, society). Deterministic: same input, same bytes.
Run from the repo root: python3 build_image.py"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (13, 37, 63)
GOLD = (198, 145, 30)
PAPER = (250, 248, 242)
CARD = (255, 255, 255)
INK = (26, 26, 26)
GREY = (100, 100, 100)
LINE = (210, 205, 195)
RED = (185, 28, 28)

# (kicker, accent colour, headline, detail)
STORIES = [
    ("SHENZHEN \u00b7 SUMMIT", (15, 118, 110),
     "Trump, Xi and Putin hold first three-way summit",
     "Four-point peace declaration after 70 minutes of talks."),
    ("THE HAGUE \u00b7 JUSTICE", (109, 40, 217),
     "World Court: Myanmar guilty of Rohingya genocide",
     "9\u20136 ruling, the first against a state for genocide."),
    ("KYIV \u00b7 WAR", RED,
     "Russian missiles hit three Kyiv bridges",
     "Three killed, 15 hurt; 100+ missiles fired overnight."),
    ("CRIMEA \u00b7 WAR", RED,
     "Ukraine hits Crimea Bridge a third time",
     "Rail halted; Putin vows a \u2018far more painful\u2019 reply."),
    ("RIYADH \u00b7 MIDEAST", (180, 83, 9),
     "Houthi missile damages Riyadh finance tower",
     "Sovereign wealth fund tower hit; no injuries."),
    ("HORMUZ \u00b7 MIDEAST", (180, 83, 9),
     "Tanker burns in Hormuz after mine strike",
     "Iran war in ninth month; US cost put at $48.3bn."),
    ("ANTALYA \u00b7 CLIMATE", (21, 128, 61),
     "COP31 talks end deadlocked on final day",
     "Fossil-fuel wording stripped; 21 issues unresolved."),
    ("ODISHA \u00b7 DISASTER", (14, 116, 144),
     "Cyclone Akvan makes landfall in India",
     "Winds 70\u201380 kmph; third cyclone in a month."),
    ("POLAND \u00b7 EUROPE", (15, 118, 110),
     "Unknown objects fall near Ukraine border",
     "Jets scrambled; Tusk says no air threat now."),
    ("GAZA \u00b7 CONFLICT", RED,
     "Israeli troops cross Gaza ceasefire line",
     "First incursion since the truce began."),
    ("BERLIN \u00b7 EUROPE", (15, 118, 110),
     "Allies meet, say Europe ready to talk to Russia",
     "Coalition of the willing agrees united position."),
    ("NEW YORK \u00b7 MARKETS", (29, 78, 216),
     "Anthropic jumps 17% in Nasdaq debut",
     "Record $81.3bn IPO values the firm at $1.5tn."),
    ("GLOBAL MARKETS", (29, 78, 216),
     "Stocks fall for a fifth straight day",
     "S&P \u22122%, Nikkei \u22124.8%, SoftBank \u221216%."),
    ("BRAZIL \u00b7 SOCIETY", (190, 24, 93),
     "Lula recognises ancestral land of Chief Raoni",
     "President Lula recognises Kayapo and Yudja ancestral lands."),
    ("BRUSSELS \u00b7 POLITICS", (15, 118, 110),
     "UK and EU set to agree youth mobility scheme",
     "Deal expected at Friday\u2019s Brussels summit."),
    ("CALIFORNIA \u00b7 TECH", (77, 124, 15),
     "Nvidia probed after CEO Huang resigns",
     "State subpoenas chipmaker over tech reaching China."),
    ("TOKYO \u00b7 ECONOMY", (29, 78, 216),
     "Japan inflation highest this year",
     "Core prices keep a rate hike on track."),
    ("SUDAN \u00b7 CONFLICT", RED,
     "Drone strike kills 10 at Sudan gold mine",
     "Attack hits Bajoun site in South Kordofan."),
]


def font(size, bold=False):
    return ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""),
        size)


def wrap(draw, text, fnt, width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def build(path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.text((W // 2, 30), "THE WORLD IN ONE PAGE",
           font=font(22, True), fill=GOLD, anchor="mt")
    d.text((W // 2, 56), "FRIDAY 20 NOVEMBER 2026",
           font=font(46, True), fill=(255, 255, 255), anchor="mt")
    d.text((W // 2, 116), "Eighteen stories that defined the day \u2014 six continents",
           font=font(20), fill=(200, 210, 225), anchor="mt")
    # grid: 3 columns x 6 rows
    x0, y0, cw, ch, gx, gy = 28, 160, 314, 121, 12, 10
    for i, (kicker, colour, head, detail) in enumerate(STORIES):
        r, c = divmod(i, 3)
        x = x0 + c * (cw + gx)
        y = y0 + r * (ch + gy)
        d.rectangle([x, y, x + cw, y + ch], fill=CARD, outline=LINE, width=1)
        d.rectangle([x, y, x + cw, y + 5], fill=colour)
        d.text((x + 12, y + 12), kicker, font=font(13, True), fill=colour)
        hl = wrap(d, head, font(18, True), cw - 24)[:2]
        ty = y + 34
        for ln in hl:
            d.text((x + 12, ty), ln, font=font(18, True), fill=INK)
            ty += 21
        dl = wrap(d, detail, font(13), cw - 24)[:2]
        for ln in dl:
            d.text((x + 12, ty), ln, font=font(13), fill=GREY)
            ty += 16
    # footer
    d.line([28, 950, W - 28, 950], fill=LINE, width=1)
    d.text((W // 2, 960),
           "Sources: BBC, Reuters, AP, CNN, UN News, One Turn \u2014 all stories dated Friday 20 November 2026",
           font=font(14), fill=GREY, anchor="mt")
    img.save(path, "PNG")


if __name__ == "__main__":
    build("entry.png")
    print("wrote entry.png")
