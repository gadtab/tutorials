dataValid = False

while dataValid == False:
    grade1 = input("Type the grade of the first test: ")
    try:
        grade1 = float(grade1)
    except:
        print (grade1, "is an invalid number")
        continue
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        dataValid = True
        
dataValid = False

while dataValid == False:
    grade2 = input("Type the grade of the second test: ")
    try:
        grade2 = float(grade2)
    except:
        print (grade2, "is an invalid number")
        continue
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        dataValid = True

dataValid = False

while dataValid == False:
    totalClasses = input("Type the total number of classes: ")
    try:
        totalClasses = int(totalClasses)
    except:
        print (totalClasses, "is an invalid number")
        continue
    if totalClasses <= 0:
        print("The number of classes can't be zero or less")
        continue
    else:
        dataValid = True

dataValid = False

while dataValid == False:
    absences = input("Type the number of absences: ")
    try:
        absences = int(absences)
    except:
        print (absences, "is an invalid number")
        continue
    if absences < 0 or absences > totalClasses:
        print("The number of absences can't be less than zero or greater than the number of total classes")
        continue
    else:
        dataValid = True


avgGrade = (grade1 + grade2) / 2
attendance = (totalClasses - absences) / totalClasses

print ("Average grade:", round(avgGrade, 2))
print ("Attendance rate:", str(round((attendance * 100), 2)) + '%')

if (avgGrade >= 6 and attendance >= 0.8):
    print("The student has been approved.")
elif (avgGrade < 6 and attendance < 0.8):
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%.")    
elif (attendance >= 0.8):
    print("The student has failed due to an average grade lower than 6.0.")
else:
    print("The student has failed due to an attendance rate lower than 80%.")
