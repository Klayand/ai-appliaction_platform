import time
import requests
import os


def text_to_audio(text, headers):
    # os.environ['http_proxy'] = "http://127.0.0.1:19180"

    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"

    payload = {
        'inputs': f'{text}'
    }

    timestamp = time.time()

    response = requests.post(API_URL, headers=headers, json=payload)

    with open(f'audio/{timestamp}.wav', 'wb') as file:
        file.write(response.content)

    audio_name = f'audio/{timestamp}.wav'
    return audio_name
