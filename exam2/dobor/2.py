from concurrent.futures import ThreadPoolExecutor
from django.contrib.sites import requests


def cat(num):
    img_url = requests.get('https://aws.random.cat/meow').json().get('file')
    with open(f'cats/cat{num}.jpg', 'wb') as file:
        file.write(requests.get(img_url).content)


def multithreading():
    with ThreadPoolExecutor(max_workers=4) as executor:
        for count in range(51):
            executor.submit(cat, count)
