import time
import requests


def text_to_audio(text, proxies, headers):

    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"

    payload = {
        'inputs': f'{text}'
    }

    timestamp = time.time()

    response = requests.post(API_URL, headers=headers, json=payload, proxies=proxies)

    with open(f'audio/{timestamp}.wav', 'wb') as file:
        file.write(response.content)

    audio_name = f'audio/{timestamp}.wav'
    return audio_name
