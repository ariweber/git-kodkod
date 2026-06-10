import requests



response = requests.get("https://jsonplaceholder.typicode.com/users/1" )

data = response.json()


name = data["name"]
email =data["email"]
city = data["address"]["city"]
print({"name": name, "email": email, "city": city }) 

# parmes = {"users": 1, "id": 1}
response1 = requests.get("https://jsonplaceholder.typicode.com/posts")

data = response1.json()

print (len(data))

response2 = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")

data = response2.json()

for user in data:
    print(user["title"])


















