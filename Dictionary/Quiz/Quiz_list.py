
Questions = ["Which car manufacturer created the first mass-produced car with a hybrid powertrain?",
         "What was the first car to feature seat belts as a standard safety feature?",
         "What is the name of the first automobile produced by Henry Ford?",
         "What car manufacturer makes rolls royce cars now?",
         "What is the highest speed ever achieved by a production car? Clue - Bugatti",
         "What is the name of the luxury car division of Honda?"]

Answers = ["D", "C", "A", "B", "A", "D"]

Options = [["A. Porsche", "B. Lamborghini", "C. Skoda", "D. Toyota"],
           ["A. Audi", "B. Mahindra", "C. Skoda", "D. Pagani"],
           ["A. Model T", "B. Model A", "C. Quadricycle", "D. Sceptical"],
           ["A. Rolls Royce, duh","B. BMW", "C. Audi", "D. Toyota"],
           ["A. 431 MPH", "B. 333 MPH", "C. 357 MPH", "D. 493 MPH"],
           ["A. Land Rover", "B. Lexus", "C. Jaguar", "D. Acura"]]
def quiz_maker(questions, answer, options):
    qa = dict(zip(questions, answer))
    qo = dict(zip(questions, options))
    print("-"*20, "CAR QUIZ", "-"*20)
    Score = 0
    for index, take in enumerate(qo):
        print(str(index + 1) + ")",take)
        for given in qo[take]:
            print(given)
        user_ans = input("Enter Your Answer - ")
        user_ans = user_ans.capitalize()
        if user_ans == qa[take]:
            Score += 1
            print("Yes! That Is The Correct Answer")
            print("Score_file - ", Score)
        else:
            print("No, That Is Not The Right Answer. :(")
            print("The Right Answer Is - ", qa[take])
            print("Score_file - ", Score)

    print("\n")
    print("Congratulations, You got", Score, "out of", len(questions))
    print("-"*20, "THE END", "-"*20)

if __name__ == "__main__":
    print(quiz_maker(Questions, Answers, Options))