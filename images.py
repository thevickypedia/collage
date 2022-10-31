import os
import warnings

from PIL import Image, ImageDraw, ImageFont

SOURCE = os.path.join(os.getcwd(), 'src')
MAX_IMAGES = 54

background_color = (255, 255, 255, 255)
pixel = (1920, 1080)
collage = Image.new(mode="RGBA", size=pixel, color=background_color)
height = width = 180

coming_soon = os.path.join(SOURCE, "coming_soon.jpg")
font_file = os.path.join(os.getcwd(), "arial.ttf")
font_size = 25


def collage_maker(filename: str = 'collage'):
    """Creates a collage with numbers images.

    References:
        HEIC to JPG: 'https://freetoolonline.com/heic-to-jpg.html'
    """
    offset = 1
    if os.path.isfile(font_file):
        font = ImageFont.truetype(font=font_file, size=font_size)
    else:
        font = ImageFont.load_default()
    for i in range(0, pixel[0], height):
        for j in range(0, pixel[1], width):
            if offset > MAX_IMAGES:
                warnings.warn(
                    "Collage dimension is larger than the combined size of individual images provided."
                )
                break
            file = os.path.join(SOURCE, f"{offset}.jpg")
            if not os.path.isfile(file) and os.path.isfile(coming_soon):
                file = coming_soon  # Adds coming soon label
            elif not os.path.isfile(file):
                raise RuntimeWarning(
                    "Neither image file nor a coming soon label is available!"
                )
            photo = Image.open(fp=file).convert("RGBA")
            photo = photo.resize(size=(height, width))
            draw = ImageDraw.Draw(im=photo)
            if offset >= 10:
                draw.rectangle(xy=(10, 10, 45, 40), fill="white")  # White background for the text to be inserted
                draw.text(xy=(13, 10), text=f"{offset}", fill=(0, 0, 0), font=font)  # Position of 2-digit numbers
            else:
                draw.rectangle(xy=(10, 10, 40, 40), fill="white")  # White background for the text to be inserted
                draw.text(xy=(20, 10), text=f"{offset}", fill=(0, 0, 0), font=font)  # Position of 1-digit numbers
            collage.paste(im=photo, box=(i, j))
            offset += 1
    collage.show()
    collage.save(fp=f"{filename}.png")


if __name__ == '__main__':
    collage_maker()
