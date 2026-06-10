import requests

posts_rsp = requests.get("https://jsonplaceholder.typicode.com/posts")

users_rsp = requests.get("https://jsonplaceholder.typicode.com/users")

dict_id_username = {}

users = users_rsp.json()
posts = posts_rsp.json()

for user in users:
    dict_id_username[user["id"]]= user["name"]

print(dict_id_username)    

for post in posts:
    print({dict_id_username[post["userId"]]: post["title"]})


