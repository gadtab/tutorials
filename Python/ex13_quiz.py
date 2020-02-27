import requests as req
import json
import random
import html

url = "https://opentdb.com/api.php?amount=1" #&category=12&difficulty=easy&type=multiple"

print("Welcome to the quiz.")
r = req.get(url)

scoreCorrect = 0
scoreIncorrect = 0

while True:
    if r.status_code != 200:
        print("There has been a problem")
        break

    validAnswer = False
    answerNumber = 1
    question = json.loads(r.text)
    print("The category is:", question['results'][0]['category'])
    print(html.unescape(question['results'][0]['question']) + ":\n")

    answers = question['results'][0]['incorrect_answers']
    correct_answer = question['results'][0]['correct_answer']
    #index = random.randint(0, len(answers))
    answers.append(correct_answer)
    random.shuffle(answers)

    for answer in answers:
        print(str(answerNumber) + " - " + html.unescape(answer))
        answerNumber += 1

    while validAnswer == False:
        userAnswer = input("Choose the number of the correct answer: ")
        try:
            userAnswer = int(userAnswer)
            if userAnswer > len(answers) or userAnswer <= 0:
                print("Invalid answer.")
            else:
                validAnswer = True
        except:
            print("Invalid answer. Use only numbers.")

    userAnswer = answers[int(userAnswer) - 1]
    if userAnswer == correct_answer:
        scoreCorrect += 1
        print ("\nYou have answered correctly. The correct answer is:", html.unescape(correct_answer))
    else:
        print ("\nYour answer", html.unescape(userAnswer), "is incorrect. The correct answer is:", html.unescape(correct_answer))
        scoreIncorrect += 1

    print("\n#####################")
    print("Your score is:")
    print("Correct answers:", scoreCorrect)
    print("Incorrect answers:", scoreIncorrect)
    print("#####################")
    
    ansQuit = input("\nPlay again? (type 'quit' to quit or just press enter to continue): ").lower()
    if ansQuit == 'quit':
        break;

    r = req.get(url)

print ("\nThanks for playing")
