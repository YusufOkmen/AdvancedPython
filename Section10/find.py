from bs4 import BeautifulSoup

with open("index.html") as file:
    html = file.read()

object = BeautifulSoup(html, "html.parser")

result = object.find_all("div")
result = len(object.find_all("div"))
result = object.find_all("div")[2].h2
result = object.find_all("div")[2].ul.find_all("li")[2]

for div in object.find_all("div"):
    if div.h2.a != None:
        print(div.h2.a.string)
    else:
        print(div.h2.string.strip())


