import requests

def safe_get(url):
    response = requests.get(url)
    data = response.json()
    status = response.status_code
    if status == 200:
        return data
    elif status == 404:
        return None
    else:
        raise "EROOR"
    
print(safe_get("https://jsonplaceholder.typicode.com/posts/999"))