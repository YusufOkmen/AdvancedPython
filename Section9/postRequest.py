import requests

sending = requests.post("https://jsonplaceholder.typicode.com/albums", data = {
    "userId": "1",
    "title": "new album"
})

result = (sending)
result = sending.text
result = sending.json()

print(result)
