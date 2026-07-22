from flask import Flask, request, send_file, abort
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.post("/sanitize")
def sanitize():
    raw = request.get_data(cache=False, parse_form_data=False)

    if not raw:
        abort(400, "No image data received")

    try:
        source = Image.open(BytesIO(raw))


        # Decode pixels into a new image object.
        # Do not copy EXIF, XMP, IPTC, GPS, comments, or other metadata.
        clean = Image.new("RGB", source.size)
        clean.putdata(source.convert("RGB").getdata())

        output = BytesIO()
        clean.save(
            output,
            format="JPEG",
            quality=95,
            optimize=True
        )
        output.seek(0)

        return send_file(
            output,
            mimetype="image/jpeg",
            download_name="sanitized.jpg"
        )

    except Exception:
        abort(400, "Invalid or unsupported image")
