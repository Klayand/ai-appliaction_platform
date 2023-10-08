import requests
from utils import headers, proxies
from dotenv import find_dotenv, load_dotenv


def summarize(text: str):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

    payload = {
        "inputs": f"{text}"
    }

    response = requests.post(API_URL, headers=headers, json=payload, proxies=proxies)

    words = response.json()
    return words




