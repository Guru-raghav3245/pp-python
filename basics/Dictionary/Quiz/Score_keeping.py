import random
"""
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
            print("Score_file - ", score)
        else:
            print("Sorry, That was not the correct answer!")
            print("Score_file - ", score)

        ask = input("Enter to continue")
        if ask == "":
            continue
        else:
            exit()"""


def add_score(score, name):
    file_bank = open("Score_file", "a")
    file_bank.write(score)
    file_bank.write(",")
    file_bank.write(name)
    file_bank.write("\n")
    file_bank.close()
    print("Done")



def print_max_score():
    file_bank = open("Score_file", "r")
    max = [1, "a"]
    for score in file_bank:
        score = score.split(",")
        score[0] = int(score[0])
        if score[0] > max[0]:
            max[0] = int(score[0])
            max[1] = score[1].replace("\n", "")

    print(max[1], "got the maximum score of", max[0])


if __name__ == "__main__":
    add_score("813", "Aaron")
    print_max_score()

def print_daddy_max_score():
    file_bank = open("Score_file", "r")
    username = ""
    maxScore = 0
    for line in file_bank:
        values = line.split(",")
        score = int(values[0])
        if score > maxScore:
            maxScore = score
            username = values[1].replace("\n", "")

    print(username, "got the maximum score of", maxScore)