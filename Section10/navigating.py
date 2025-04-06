from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

object = BeautifulSoup(html, "html.parser")

result = object.body.div.contents[3]

result = object.body.div.children # Give me the first childrens of div tag
# for obj in result:
#     print(obj)

result = object.body.div.descendants # Give me all the childrens of div rag
# for obj in result:
#     print(obj)

result = object.body.h2.parent # Give me the parent of h2 tag

result = object.body.h2.next_element.next_element # Go right below of h2

result = object.body.div.h2.next_sibling.next_sibling # Get me sibling of the h2

result = object.body.div.find_next_sibling("div").find_previous_sibling("div") # Get me next or previous sibling of the div which is div

print(result)