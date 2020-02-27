person = {"name": "gadi tabachnik", "gender": "male", "age": 44, "address": "uzi narkis 5, kfar sava", "phone": "050-8846912"}

key = input("what do you want to know about this person? ").lower()

value = person.get(key, "invalid property")

print("The person's", key, "is", value)
