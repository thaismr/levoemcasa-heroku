from PIL import Image


def img_resize(img_path, new_width):
    img = Image.open(img_path)
    width, height = img.size

    if width > new_width:
        new_height = round(
            (new_width * height) / width
        )
        img = img.resize((new_width, new_height), Image.LANCZOS)

    img.save(img_path, optimize=True, quality=60)
    img.close()
