import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

result = response
result = response.headers
result = response.url
result = response.encoding
result = response.text
posts = json.loads(response.text)
result = posts

for item in posts:
    if item["userId"] == 1:
        print(item["title"])

# print(result)