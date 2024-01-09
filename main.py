import os

from pilmoji import Pilmoji
from PIL import Image, ImageFont
from flags import flags

# ---------- CONFIGURE STUFF HERE ----------------

img_size = 128

font_size = 24
emoji_scale_factor = 4
emoji_offset = font_size * emoji_scale_factor // 2

output_dir = f"images"

# ----------- END OF CONFIGURATION ---------------


if not os.path.exists(output_dir):
    print(f"Creating destination directory {output_dir}")
    os.mkdir(output_dir)

for state, flag in list(flags.items()):
    state = state.replace(" ", "_")

    if not state.isascii():
        # Probably illegal file name
        print("NOT ASCII:", state, "- skipping")
        continue

    print(state, flag)

    with Image.new('RGBA', (img_size, img_size), (255, 255, 255, 0)) as image:
        font = ImageFont.truetype('arial.ttf', font_size)

        with Pilmoji(image) as pilmoji:
            pilmoji.text((img_size // 2 - emoji_offset, img_size // 2 - emoji_offset),
                         flag,
                         (0, 0, 0),
                         font,
                         emoji_scale_factor=emoji_scale_factor)

        with open(f"{output_dir}/{state}.png", "wb") as f:
            image.save(f, "png")
