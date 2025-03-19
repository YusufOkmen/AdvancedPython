import re 

text = "4ABD 123 XYZ 456 @&% 300 2 340000 1_2 22_3 A1AA"

# pattern = r"\d\d\d"
# pattern = r"\d+"
# pattern = r"\d*"
# pattern = r"\d{3}"
# pattern = r"\d{3,5}"
# pattern = r"\d{,5}"
# pattern = r"\d.\d"
# pattern = r"[a-z]"
# pattern = r"[a-zA-Z0-9]"
# pattern = r"[a-z]"
# pattern = r"\d|[a-z]"
# pattern = r"\d\w\w"
# pattern = r"^\d\w\w"
# pattern = r"^A\d\w\w"
pattern = r"A\d\w\w$"

matches = re.search(pattern, text)
matches = re.findall(pattern, text)
matches = re.finditer(pattern, text)

for match in matches:
    print(match)
