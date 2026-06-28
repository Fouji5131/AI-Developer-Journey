import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
print("Status:", response.status_code)
print("Response:", response.json())
