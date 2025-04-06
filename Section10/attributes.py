from bs4 import BeautifulSoup

with open("index.html") as file:
    html = file.read()

object = BeautifulSoup(html, "html.parser")

result = object
result = object.find(id="item1")
result = object.find(id="header")
result = object.find(class_="item")
result = object.find_all(class_="item")

result = object.select("#header") # Give me the objects that has id as "header"
result = object.select("#item1")
result = object.select(".red") # Give me the objects that has class as "red"
result = object.select_one(".item") # Give me the first object that has class as "item"

result = object.div.attrs["class"] # Give me the name of class attributes of the first div
result = object.div.attrs["id"]

result = object.div.get_text(strip=True, separator=",")

for a in object.find_all("a"):
    print(a.get("href"))
