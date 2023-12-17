import requests

headers = {'Authorization': 'Bearer 0a9116c16bb6b0e31871abde03a2f7cbe5204ae4'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is Title Field Entry",
    "price": 28.99
}
get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
