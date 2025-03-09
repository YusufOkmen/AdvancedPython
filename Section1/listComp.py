# List Comperehensions: It is important for cleaner code.

numbers1 = []
for i in range(5):
    numbers1.append(i)
print(numbers1)

numbers2 = [i for i in range(5)]
print(numbers2) # Lesser code than numbers1 list.

""""""

company = "Okmen Company"
for i in company:
    print(i.upper())

result = [i.upper() for i in company]
print(result)