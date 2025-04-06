from bs4 import BeautifulSoup

with open("index.html") as file:
    html = file.read()

object = BeautifulSoup(html, "html.parser")

result = type(object)
result = type(html)
result = object.prettify()
result = object.title
result = object.title.string
result = object.body.h1.string
result = object.div

print(result)