import re 

text = "My name is Yusuf Ökmen I live in Türkiye my birth date is 01/12/2000 my phone number is +90-590-999-9999 +90 591 999 9999 my mail adress is yusufokkmen@gmail.com yusufkmen@hotmail.com.tr"

# pattern = r"\d{2}[-./]([a-zA-Z0-9]{3}|\d{2})[-./]\d{4}"
# pattern = r"[a-z]{3,20}@[a-z]{3,20}\.(com|tr)"
# pattern = r"\w+@[a-z]+(\.[a-z]{2,3})+" 
pattern = r"\+\d{2}[-\s]\d{3}[-\s]\d{3}[-\s]\d{4}"

matches = re.finditer(pattern, text)

for match in matches:
    print(match)