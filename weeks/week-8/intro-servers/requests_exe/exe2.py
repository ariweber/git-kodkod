import requests
new_post = {
"title": "My First Post",
"body": "This is the content",
"userId": 1
}
response = requests.post(
"https://jsonplaceholder.typicode.com/posts",
json=new_post )
print(response.status_code) # 201 Created
print(response.json()) 
