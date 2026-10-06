from pathlib import Path

import qrcode


def generate_qr(data, filename):
    output_path = Path(filename)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    img = qrcode.make(data)
    img.save(output_path)
