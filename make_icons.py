from PIL import Image, ImageDraw

WATER = (11, 27, 34)
ORANGE = (255, 90, 31)
RED = (192, 38, 45)
WHITE = (255, 255, 255)
TEAL = (47, 168, 160)


def draw_icon(size, maskable=False):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # background rounded square (full bleed for maskable)
    r = size // 5
    d.rounded_rectangle([0, 0, size, size], radius=0 if maskable else r, fill=WATER)

    # water ripples
    cx = size // 2
    water_y = int(size * 0.62)
    for i in range(3):
        y = water_y + i * int(size * 0.06)
        d.line([(int(size * 0.12), y), (int(size * 0.88), y)],
               fill=(TEAL[0], TEAL[1], TEAL[2], 90), width=max(1, size // 90))

    # float (poplavok): antenna + body + base, standing on water
    w = max(2, size // 22)
    top = int(size * 0.20)
    # orange antenna
    d.rectangle([cx - w // 2, top, cx + w // 2, int(size * 0.42)], fill=ORANGE)
    # white ring
    d.rectangle([cx - w, int(size * 0.42), cx + w, int(size * 0.47)], fill=WHITE)
    # red body (teardrop-ish)
    body_top = int(size * 0.47)
    body_bot = water_y
    d.rounded_rectangle([cx - int(w * 1.6), body_top, cx + int(w * 1.6), body_bot],
                        radius=w, fill=RED)
    # tip below water (reflection hint)
    d.polygon([(cx - w, water_y), (cx + w, water_y), (cx, int(size * 0.72))],
              fill=(ORANGE[0], ORANGE[1], ORANGE[2], 120))
    return img


for s in (192, 512):
    draw_icon(s).save(f"icons/icon-{s}.png")
draw_icon(512, maskable=True).save("icons/icon-512-maskable.png")
draw_icon(180).save("icons/apple-touch-icon.png")
print("icons done")
