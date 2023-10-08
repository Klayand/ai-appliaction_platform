import requests


def summarize(text: str, proxies, headers):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

    payload = {
        "inputs": f"{text}"
    }

    response = requests.post(API_URL, headers=headers, json=payload, proxies=proxies)

    words = response.json()
    return words




