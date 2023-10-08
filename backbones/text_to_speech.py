import requests
import time
import os


def text_to_speech(sentence, headers):
    API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"

    # os.environ['http_proxy'] = os.getenv('HTTPS_PROXY')

    payloads = {
        "inputs": sentence
    }
    timestamp = time.time()

    response = requests.post(API_URL, json=payloads, headers=headers)
    with open(f'speech/{timestamp}.wav', 'wb') as file:
        file.write(response.content)

    speech_name = f'speech/{timestamp}.wav'

    return speech_name
