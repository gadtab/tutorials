import time as t
import random as r
import matplotlib.pyplot as plt

words = ["cakes", "cages", "agile", "altar", "english"]
index = r.randint(0, len(words)-1)

word = words[index]

#wordsCorrect = []
mistakesCount = 0
timeTook = []
typedWords = []

print("Try to type the word", word, "5 times, as fast as posible")
input("Press enter to start!")

for i in range(5):
    start = t.time()
    typedWord = input("Try #" + str((i + 1)) + ": ")
    #took = t.time - start
    timeTook.append(round((t.time() - start), 2))
    typedWords.append(typedWord)
    if word != typedWord.lower():
        mistakesCount += 1


#print(typedWords)
print("You made", mistakesCount, "mistake(s)")
#print(timeTook)
print ("Now lets see your evolution")
t.sleep(3)
x = ["try 1", "try 2", "try 3" , "try 4", "try 5"]

plt.plot(x, timeTook)

plt.ylabel('Time in seconds')
plt.xlabel('Attempts')
plt.title('Your typing evolution')
plt.show()
