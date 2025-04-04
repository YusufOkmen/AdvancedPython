import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos", params= {
    "userId": "4", 
    "completed": "true"
})

result = response
result = response.json()

print(result)