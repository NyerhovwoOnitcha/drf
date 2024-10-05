import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "https://httpbin.org/"
#endpoint = "https://httpbin.org/status/200"

r = requests.get(endpoint, json={"query": "Hello world"})
#print(r.text) # print the raw text response

#print(r.json())

print(r.status_code)




# # endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

# get_response = requests.get(endpoint, json={"query": "Hello world"}) # HTTP Request
# print(get_response.text) # print raw text response


# # HTTP Request -> HTML
# # REST API HTTP Request -> JSON
# # JavaScript Object Nototion ~ Python Dict
# print(get_response.json())
# print(get_response.status_code