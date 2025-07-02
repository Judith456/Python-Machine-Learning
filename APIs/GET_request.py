import requests

#response = requests.get('https://api.github.com')
response = requests.get('https://jsonplaceholder.typicode.com/posts')

#print the status code and the JSON response
print("Status Code:", response.status_code)
print("\n")
print("Response JSON:", response.text)
#print("Response JSON:", response.json())

