import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://quotes.toscrape.com/"

response = requests.get(url)

html = BeautifulSoup(response.text, "html.parser")

quotes = html.find_all(class_="col-md-8")[1].find_all(class_="quote")

with open("quotes.csv", "w", encoding="utf-8") as file:
    csvWriter = writer(file)
    csvWriter.writerow(["authors", "quotes", "tags"])



    for quote in quotes:
        authors = quote.find(class_="author").string
        aList = []
        tags = quote.find(class_="tags").find_all(class_="tag")
        for a in tags:
            newA = a.string
            aList.append(newA)         
        sentence = quote.find(class_="text").string
        
        csvWriter.writerow([authors, sentence, aList])
