import random
def create_ques_bank():
    ques1 = "Which car manufacturer created the first mass-produced car with a hybrid powertrain?"
    ans1 = ["Toyota", "Lamborghini", "Skoda", "Porsche"]

    ques2 = "What was the first car to feature seat belts as a standard safety feature?"
    ans2 = ["Skoda", "Mahindra", "Audi", "Pagani"]

    ques3 = "What is the name of the first automobile produced by Henry Ford?"
    ans3 = ["Model T", "Model A", "Quadricycle", "Sceptical"]

    ques4 = "What car manufacturer makes rolls royce cars now?"
    ans4 = ["BMW", "Rolls Royce, duh", "Audi", "Toyota"]

    ques5 = "What is the highest speed ever achieved by a production car? Clue - Bugatti"
    ans5 = ["431 MPH", "333 MPH", "357 MPH", "493 MPH"]

    ques6 = "What is the name of the luxury car division of Honda?"
    ans6 = ["Acura", "Lexus", "Jaguar", "Landrover"]

    ques7 = "What does the acronym RPM stand for in a car?"
    ans7 = ["Revolutions per minute", "Rear power module", "Road performance mechanism", "Rapid power movement"]

    ques8 = "Which of the following car brands is headquartered in Germany?"
    ans8 = ["BMW", "Toyota", "Ford", "Corvette"]

    questions = [ques1, ques2, ques3, ques4, ques5, ques6, ques7, ques8]
    answers = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8]

    question_answer_bank = dict(zip(questions, answers))

    return question_answer_bank

def askquiz(ques_bank):
    score = 0
    for index, question in enumerate(ques_bank):
        ans = ques_bank[question][0]
        options = ques_bank[question]
        print(question)
        random.shuffle(options)

        for index, i in enumerate(options):
            print(index+1, i)

        userinput = input("What is your answer - ")
        if str(options[int(userinput) - 1]) == str(ans):
            score += 1
            print("Congratulations, You got the answer right")
            print("Score - ", score)
        else:
            print("Sorry, That was not the correct answer!")
            print("Score - ", score)

        ask = input("Enter to continue")
        if ask == "":
            continue
        else:
            exit()

if __name__ == "__main__":
    my_q_bank = create_ques_bank()
    your_score = askquiz(my_q_bank)

