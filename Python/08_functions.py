def sayHello(person1, person2="The director"):
    print("Hello", person1 + ", how are you doing?", person2, "is waiting for you.")

def fahr2celsius(fahr):
    celsius = (5 * (fahr -32) / 9)
    return celsius

sayHello("Gadi", "Lia")
sayHello("Andi", "Tamar")
sayHello("Oren")

print("Celsius:", round(fahr2celsius(100), 2))
print("Kelvin:", round(fahr2celsius(100) + 273.5, 2))
