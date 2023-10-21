import requests

ENDPONINT = 'http://127.0.0.1:8000/products/1/'

RESP = requests.get(ENDPONINT)

print(RESP.json())