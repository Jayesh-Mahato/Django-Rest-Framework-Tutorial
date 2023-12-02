import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

# HTTP Request
get_response = requests.get(endpoint, json={"query:":"Hello World"}) 
get_response2 = requests.get(endpoint, data={"query:":"Hello World"}) 
# print(get_response.text) # print raw text response

# print(get_response.json())
print(get_response.status_code)


