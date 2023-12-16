import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# HTTP Request
# get_response = requests.get(endpoint, params={"abc": 123}, json={"query:":"Hello World"}) 
# get_response2 = requests.get(endpoint, data={"query:":"Hello World"}) 
# print(get_response.text) # print raw text response
get_response = requests.get(endpoint, json={"product_id:": 123})

# print(get_response.json())
# print(get_response.status_code)
print(get_response.json())
# print(get_response.json()['message'])


