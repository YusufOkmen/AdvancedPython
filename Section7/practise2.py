
with open("example.txt", "a") as file:
    file.write("Yusuf\n")
    file.write("Ökmen\n")


with open("example.txt", "r") as file:

    content = file.read()

    print(content)

