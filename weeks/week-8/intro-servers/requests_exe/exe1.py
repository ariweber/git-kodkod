import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()
print(data["title"]) # the post title
print(data["userId"]) 



