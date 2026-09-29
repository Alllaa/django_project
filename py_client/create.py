import requests

endpoints =  'http://localhost:8000/api/products/'

data ={'title': 'item3','price':13.42}
get_response = requests.post(endpoints, data=data)

print(get_response.json())
