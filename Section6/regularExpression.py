import re

text = "Advanced Python Course Python"
pattern = "Python"

match = re.search(pattern, text)

allMatch = re.findall(pattern, text)

print(match)

print(allMatch)

print(text[9:15])