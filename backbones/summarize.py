import requests
import os


def summarize(text: str, proxies, headers):
    os.environ['http_proxy'] = "http://127.0.0.1:19180"
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

    payload = {
        "inputs": f"{text}"
    }

    response = requests.post(API_URL, headers=headers, json=payload, proxies=proxies)

    words = response.json()
    return words




