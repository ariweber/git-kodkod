import requests
# PUT — replace the entire resource
updated = {"id": 1, "title": "New Title", "body": "New content", "userId":
1}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated)

print(response.status_code) # 200 OK
print(response.json()) # the updated post
