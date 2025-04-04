import requests

url = "http://api.weatherapi.com/v1/current.json"
key = "ed53d95136044af0800162239250404"

location = input("Locaiton: ")
 
response = requests.get(url, params= {
    "key": key,
    "q": location
})

resultJson = response.json()
city = resultJson["location"]["name"]
heat = resultJson["current"]["temp_c"]
text = resultJson["current"]["condition"]["text"]

print(f"{city} is {heat} Celcius right now.")

