import requests

endpoint = "http://localhost:8080/drinks/"

get_response = requests.get(endpoint)
print(get_response.json())