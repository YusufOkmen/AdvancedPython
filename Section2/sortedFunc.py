# sorted Func: is useful when we want to sort big data sets. Sorted function opens a new list and passes the value.

users = [
    {"username": "Yusuf", "posts": ["post1", "post2"], "email": "yusufokkmen@gmail.com", "phone": "12213132"},
    {"username": "Abdullah", "posts": ["post1", "post2", "post3"], "email": "abdullahokmen@gmail.com"},
    {"username": "Elif", "posts": ["post1"]},
]

sortedUsers = sorted(users, key=len) # This is a list which is sorted due to key's number

sortedUsers2 = sorted(users, key = lambda user: user["username"])

userList = list(map((lambda user: user["username"]), sortedUsers2))

# print(userList)


courses = [
    {"courseName": "Java", "cost": 10000}, 
    {"courseName": "Python", "cost": 4000},
    {"courseName": "C", "cost": 40000}
]

sortedCourses = sorted(courses, key = lambda course: course["cost"])

courseList = list(map((lambda course: course["courseName"]), sortedCourses))
print(courseList)