import requests
import os


def image_to_text(filename, headers):
    # os.environ['http_proxy'] = "http://127.0.0.1:19180"
    API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, data=data, headers=headers)

    return response.json()