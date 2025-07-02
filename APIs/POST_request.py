import requests

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    "title": "foo",
    "id": 101,
    "body": "bar",
    "userId": 10
}

response = requests.post(url, json=data)

print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())