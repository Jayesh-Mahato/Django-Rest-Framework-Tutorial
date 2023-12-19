import requests

headers = {'Authorization': 'Bearer ead73c9a0630b0b2218eec0eee28290e01a48db7'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is Title Field Entry",
    "price": 28.99
}
get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
