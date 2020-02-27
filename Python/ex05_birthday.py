months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

birthday = input("Please enter your birthday in the format DD-MM-YYYY: ")

month = int(birthday[3:5])

print("You were born in", months[month - 1]) 
