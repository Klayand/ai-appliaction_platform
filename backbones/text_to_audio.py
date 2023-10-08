import time
from dotenv import find_dotenv, load_dotenv
import requests
from utils import proxies, headers

load_dotenv(find_dotenv())


def text_to_audio(text):

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
