import random
# Creating a question bank from file


def create_ques_bank():
    question_list = []
    option_list = []
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


# Displaying the quiz in a structured form
def askquiz(ques_bank):
    print("-"*10, "Car Quiz", "-"*10)
    score = 0
    for index1, question in enumerate(ques_bank):
        ans = ques_bank[question][0]
        options = ques_bank[question]
        print(str(index1+1) + ". " + str(question))
        random.shuffle(options)

        for index, i in enumerate(options):
            x = str(index + 1) + "."
            print(" ", x, i)

        userinput = input("What is your answer - ")
        if str(options[int(userinput) - 1]) == str(ans):
            score += 1
            print("Congratulations, You got the answer right")
            print("Score - ", score)
        else:
            print("Sorry, That was not the correct answer!")
            print("Score - ", score)
            print("The correct answer was - ", ans)
        ask = input("  Enter to continue")
        if ask == "":
            continue
        else:
            print("Score = ", score)
            name = input("Enter your name - ")
            if name.__contains__("\n"):
                name = name.replace("\n", "")
            file_bank = open("Score_file", "a")
            file_bank.write(str(score))
            file_bank.write(",")
            file_bank.write(name)
            file_bank.write("\n")
            file_bank.close()
            exit()
    # Adding the score and name onto score file
    name = input("Enter your name - ")
    if name.__contains__("\n"):
        name = name.replace("\n", "")
    file_bank = open("Score_file", "a")
    file_bank.write(str(score))
    file_bank.write(",")
    file_bank.write(name)
    file_bank.write("\n")
    file_bank.close()
    return ""

# Listing the scores in a table form
def table():
    file_bank = open("Score_file", "r")
    score_list = []
    name_list = []
    # Getting scores from file
    for score in file_bank:
        score = score.split(",")
        score_list.append(int(score[0]))
        if score[1].__contains__("\n"):
            score[1] = score[1].replace("\n", "")
        name_list.append(score[1])

    # Arranging the list in ascending form
    dict1 = dict(zip(score_list, name_list))
    score_list.sort()
    score_list.reverse()
    print("_"*10, "Leaderboard", "_"*10)
    print("         Score      Name")
    for index, i in enumerate(score_list):
        print(str(index+1) + ".       ", score_list[index], "        ", dict1[i])
    return


"""
# Adding the score to file
def add_score(score, name):
    file_bank = open("Score_file", "a")
    file_bank.write(score)
    file_bank.write(",")
    file_bank.write(name)
    file_bank.write("\n")
    file_bank.close()
    print("Done")
    return ""
# Printing the max score of that file


def print_max_score():
    file_bank = open("Score_file", "r")
    max = [1, "a"]
    for score in file_bank:
        score = score.split(",")
        score[0] = int(score[0])
        if score[0] > max[0]:
            max[0] = score[0]
            max[1] = score[1].replace("\n", "")

    print(max[1], "got the maximum score of", max[0])
    return ""
    """


if __name__ == "__main__":
    print(askquiz(create_ques_bank()))
    print(table())
# Creating a question bank from file


def create_ques_bank():
    question_list = []
    option_list = []
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


# Displaying the quiz in a structured form
def askquiz(ques_bank):
    print("-"*10, "Car Quiz", "-"*10)
    score = 0
    for index1, question in enumerate(ques_bank):
        ans = ques_bank[question][0]
        options = ques_bank[question]
        print(str(index1+1) + ". " + str(question))
        random.shuffle(options)

        for index, i in enumerate(options):
            x = str(index + 1) + "."
            print(" ", x, i)

        userinput = input("What is your answer - ")
        if str(options[int(userinput) - 1]) == str(ans):
            score += 1
            print("Congratulations, You got the answer right")
            print("Score - ", score)
        else:
            print("Sorry, That was not the correct answer!")
            print("Score - ", score)
            print("The correct answer was - ", ans)
        ask = input("  Enter to continue")
        if ask == "":
            continue
        else:
            print("Score = ", score)
            name = input("Enter your name - ")
            if name.__contains__("\n"):
                name = name.replace("\n", "")
            file_bank = open("Score_file", "a")
            file_bank.write(str(score))
            file_bank.write(",")
            file_bank.write(name)
            file_bank.write("\n")
            file_bank.close()
            exit()
    # Adding the score and name onto score file
    name = input("Enter your name - ")
    if name.__contains__("\n"):
        name = name.replace("\n", "")
    file_bank = open("Score_file", "a")
    file_bank.write(str(score))
    file_bank.write(",")
    file_bank.write(name)
    file_bank.write("\n")
    file_bank.close()
    return ""

# Listing the scores in a table form
def table():
    file_bank = open("Score_file", "r")
    score_list = []
    name_list = []
    # Getting scores from file
    for score in file_bank:
        score = score.split(",")
        score_list.append(int(score[0]))
        if score[1].__contains__("\n"):
            score[1] = score[1].replace("\n", "")
        name_list.append(score[1])

    # Arranging the list in ascending form
    dict1 = dict(zip(score_list, name_list))
    score_list.sort()
    score_list.reverse()
    print("_"*10, "Leaderboard", "_"*10)
    print("         Score      Name")
    for index, i in enumerate(score_list):
        print(str(index+1) + ".       ", score_list[index], "        ", dict1[i])
    return


"""
# Adding the score to file
def add_score(score, name):
    file_bank = open("Score_file", "a")
    file_bank.write(score)
    file_bank.write(",")
    file_bank.write(name)
    file_bank.write("\n")
    file_bank.close()
    print("Done")
    return ""
# Printing the max score of that file


def print_max_score():
    file_bank = open("Score_file", "r")
    max = [1, "a"]
    for score in file_bank:
        score = score.split(",")
        score[0] = int(score[0])
        if score[0] > max[0]:
            max[0] = score[0]
            max[1] = score[1].replace("\n", "")

    print(max[1], "got the maximum score of", max[0])
    return ""
    """


if __name__ == "__main__":
    print(askquiz(create_ques_bank()))
    #print(table())

