blogPosts = ["", "The 10 coolest math functions in Python", "", "How to make HTTP requests in Python", "A tutorial about data types in Python"]

for post in blogPosts:
    if post == "":
        continue
    else :
        print (post)

print ("-----------------")
myString = "This is a string"

for char in myString:
    print (char)

print ("-----------------")
for x in range(0, 10):
    print (x)

print ("-----------------")
person = {"name": "gadi", "age": 44, "gender": "male"}

for key in person:
    print (key, ":", person[key])

print ("-----------------")
blogPosts = {"Python": ["The 10 coolest math functions in Python", "How to make HTTP requests in Python", "A tutorial about data types in Python"], "Javascript": ["Namespaces in Javascript", "New functions available in ES6"]}

for category in blogPosts:
    print ("Posts about", category)

    for post in blogPosts[category]:
        print (post)
