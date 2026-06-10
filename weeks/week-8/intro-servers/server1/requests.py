import requests

response = requests.get("http://localhost:8000/items/count")

print(response.status_code)

print(response.json())