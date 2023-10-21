import requests

product_id = input('Which id do you want to delete?\n')

try:
    product_id = int(product_id)
except ValueError:
    print(f"{product_id} is not an integer.")
    product_id = None

if product_id is not None:
    Endpoint = f"http://127.0.0.1:8000/products/{product_id}/delete/"

    Resp = requests.delete(Endpoint)
    if Resp.status_code == 204:
        print("Delete request was successful.",Resp.status_code)
    else:
        print("Delete request failed. Status code:", Resp.status_code)
