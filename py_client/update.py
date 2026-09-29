import requests

endpoints =  'http://localhost:8000/api/products/1/update'

data={"content":"Updated 1","title":"New Title"}
get_response = requests.put(endpoints,data=data)

print(get_response.json())
