import requests
    

headers = {'Authorization': 'Bearer34c4bf20d771cf8e89ddf355886506b32a1cf273'}
endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "this field is done",
    "price": 32.99
}
get_response = requests.post(endpoint,json=data,headers= headers)

print(get_response.json())