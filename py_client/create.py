import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is Title Field Entry",
    "price": 29.99
}
get_response = requests.post(endpoint, json=data)

print(get_response.json())
