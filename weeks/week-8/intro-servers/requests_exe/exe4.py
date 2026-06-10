import requests
# Query parameters are passed as a dict to params=
params = {"userId": 1, "id": 1}
response = requests.get(
"https://jsonplaceholder.typicode.com/posts",
params=params # becomes: /posts?userId=
)
posts = response.json()
print(posts)
print(f"Found {len(posts)} posts for user 1")
for post in posts[:3]: 
    print(f" - {post['title']}")

