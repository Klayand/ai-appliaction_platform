import requests
from ../utils import proxies, headers


def image_to_text(filename):
    API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, data=data, proxies=proxies, headers=headers)

    return response.json()
