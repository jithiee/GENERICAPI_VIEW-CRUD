import requests

ENDPOIT = 'http://127.0.0.1:8000/products/' 

data = {
    'title' : 'wowwwww',
    'price' : 520.5
    
}

resp = requests.post(ENDPOIT ,json=data)
print(resp.json())


