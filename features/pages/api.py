import requests


def send_get(url, params):
    response = requests.get('google.com')
    print(response.json())

def send_post(url, data, params):
    response = requests.post('google.com')
    print(response.json())