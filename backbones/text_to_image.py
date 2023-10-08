import requests
import io
from PIL import Image
import time


def text_to_image(text, proxies, headers):

    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

    payload = {
        'inputs': f'{text}'
    }

    timestamp = time.time()

    response = requests.post(API_URL, headers=headers, json=payload, proxies=proxies)

    image = Image.open(io.BytesIO(response.content))
    image.save(f'pic/{timestamp}.png')

    image_name = f'pic/{timestamp}.png'

    return image_name
