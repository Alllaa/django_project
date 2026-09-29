import requests

endpoints =  'http://localhost:8000/api/products/'

get_response = requests.get(endpoints)

print(get_response.json())
