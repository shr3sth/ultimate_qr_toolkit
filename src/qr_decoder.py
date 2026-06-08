from pyzbar.pyzbar import decode
from PIL import Image


def decode_qr(image_path):
    image = Image.open(image_path)

    results = decode(image)

    if not results:
        return None

    return results[0].data.decode("utf-8")
