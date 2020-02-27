import random

names = []

while len(names) < 8:
    name = input("Please enter a name: ")
    names.append(name)

ranName = random.randint(0, 8)
print (names[ranName])
