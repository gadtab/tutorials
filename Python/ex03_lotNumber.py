lotNumber = input("Please enter your lot number(xxx-xxxxx-xxxxx): ")

print("Country code:", lotNumber[:3])
print("Product code:", lotNumber[4:9])
print("Batch number:", lotNumber[10:])
