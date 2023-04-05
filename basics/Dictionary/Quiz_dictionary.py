
QandOptions = {"Which car manufacturer created the first mass-produced car with a hybrid powertrain?": ["A. Porsche", "B. Lamborghini", "C. Skoda", "D. Toyota"],
           "What was the first car to feature seat belts as a standard safety feature?": ["A. Audi", "B. Mahindra", "C. Skoda", "D. Pagani"],
           "What is the name of the first automobile produced by Henry Ford?": ["A. Model T", "B. Model A", "C. Quadricycle", "D. Sceptical"],
           "What car manufacturer makes rolls royce cars now?": ["A. Rolls Royce, duh","B. BMW", "C. Audi", "D. Toyota"],
           "What is the highest speed ever achieved by a production car? Clue - Bugatti": ["A. 431 MPH", "B. 333 MPH", "C. 357 MPH", "D. 493 MPH"],
           "What is the name of the luxury car division of Honda?": ["A. Land Rover", "B. Lexus", "C. Jaguar", "D. Acura"]}

QandA = {"Which car manufacturer created the first mass-produced car with a hybrid powertrain?": "D",
         "What was the first car to feature seat belts as a standard safety feature?": "C",
         "What is the name of the first automobile produced by Henry Ford?": "A",
         "What car manufacturer makes rolls royce cars now?": "B",
         "What is the highest speed ever achieved by a production car? Clue - Bugatti": "A",
         "What is the name of the luxury car division of Honda?": "D"}
def quiz_maker(questions, options):
    print("-"*20, "CAR QUIZ", "-"*20)
    Score = 0
    for index, take in enumerate(options):
        print(str(index + 1) + ")",take)
        for given in options[take]:
            print(given)
        ans = input("Enter Your Answer - ")
        ans = ans.capitalize()
        if ans == questions[take]:
            Score += 1
            print("Yes! That Is The Correct Answer")
            print("Score_file - ", Score)
        else:
            print("No, That Is Not The Right Answer. :(")
            print("The Right Answer Is - ", questions[take])
            print("Score_file - ", Score)

    print("\n")
    print("Congratulations, You got", Score, "out of", len(questions))
    print("-"*20, "THE END", "-"*20)

#print(quiz_maker(QandA, QandOptions))
if __name__ == "__main__":
    print(quiz_maker(QandA, QandOptions))