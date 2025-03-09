# filter Func: With map function we can transform our list elements as we want. But we have to transform all of them. With filter function we can filter the elements of the list's. It can be imaginable like if statements

numbers1 = [1, 2, -5, 3, -6, -2] 

#1
negativeNum = list(filter((lambda num: num < 0), numbers1))
# print(negativeNum)

#2
evenNum = list(filter((lambda num: num % 2 == 0), numbers1))
# print(evenNum)

names = ["joseph", "ayse", "jack", "yusuf"]

#3
jNames = list(filter((lambda name: name[0] == "j"), names))
# print(jNames)


users = [
    {"username": "Yusuf", "posts": ["post1", "post2"]},
    {"username": "Abdullah", "posts": ["post1", "post2", "post3"]},
    {"username": "Elif", "posts": ["post1"]},
]

#4
postList = list(filter((lambda user: len(user["posts"]) <= 2), users))
print(postList)
postListName = list(map((lambda name: name["username"]), postList))
print(postListName)

#5 
theUsers = [user["username"] for user in users if len(user["posts"]) <=2]
print(theUsers)