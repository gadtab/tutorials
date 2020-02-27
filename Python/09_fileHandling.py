f = open("test.txt", "a")
f.write("\nThis text will be appended to our file")

f = open("test.txt")
print(f.read())
