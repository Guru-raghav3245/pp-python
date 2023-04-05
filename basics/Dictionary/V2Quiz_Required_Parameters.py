import random
def create_ques_bank():
    question_list = []
    option_list = []
    zip_qo = []
    ques_file = open("Quiz_file", 'r')
    for question in ques_file:
# Adding question onto list
        if question.startswith("Question"):
            # question.rstrip("\n")
            if question.__contains__("\n"):
                question = question.replace("\n", "")
            if question.__contains__("Question - "):
                question = question.replace("Question - ", "")
            question_list.append(question)

# Adding options as a list onto list
            semi_final = []
            for opt in range(4):
                opt = ques_file.readline()
                if opt.__contains__("\n"):
                    opt = opt.replace("\n", "")
                semi_final.append(opt)
            option_list.append(semi_final)

    ques_file.close()
    zip_qo = dict(zip(question_list, option_list))
    return zip_qo

# return question_answer_bank

def askquiz(ques_bank):
    score = 0
    for index1, question in enumerate(ques_bank):
        ans = ques_bank[question][0]
        options = ques_bank[question]
        print(question)
        random.shuffle(options)

        for index, i in enumerate(options):
            x = str(index + 1) + "."
            print(x, i)

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

