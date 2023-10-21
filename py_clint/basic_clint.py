import requests

ENDPONT = 'http://127.0.0.1:8000/api'

resp = requests.get(ENDPONT, json={'quesry':'hello world'})
print(resp.headers)
print(resp.text)

print(resp.status_code)
print(resp.json())


