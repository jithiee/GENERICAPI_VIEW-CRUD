import requests


ENDPONINT = 'http://127.0.0.1:8000/products/list/'

data ={
    'title': 'mango',
    'content':'new mango',
    'price':25.65
}

RESP = requests.post(ENDPONINT,json=data) # post
response = requests.get(ENDPONINT) # get
print(RESP.json())
print('=========*********************=============*************==========================================')
print(response.json())
