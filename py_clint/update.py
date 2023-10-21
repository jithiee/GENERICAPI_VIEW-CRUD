import requests

ENDPONINT = 'http://127.0.0.1:8000/products/1/update/'


data ={
    
    'title':'updated ',
    'price':56.5
}


resp = requests.put(ENDPONINT,json=data)
print(resp)
print('===============================')

print(resp.json())




