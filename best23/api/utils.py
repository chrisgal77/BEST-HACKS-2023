from PIL import Image
import base64
import io

def load_image_as_base64(image_path):
    with Image.open(image_path) as img:
        if img.format != "JPEG":
            img = img.convert("RGB")

        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format="JPEG")
        img_byte_array = img_byte_array.getvalue()

        base64_image = base64.b64encode(img_byte_array).decode('utf-8')

        return base64_image