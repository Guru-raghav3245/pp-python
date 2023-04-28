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
    return score


def namechek(file, name):
    file_bank = open(file, "r")
    name_list = []
    while name == "":
        if name == "":
            name = input("Please input a valid name - ")
        else:
            break

    while True:
        if len(name) <= 3:
            name = input("Not enough characters. Please input a valid name - ")
        else:
            break

    while True:
        if name.isalpha():
            break
        else:
            name = input("Please input a valid name - ")

    while True:
        for line in file_bank:
            score, name1 = line.split(",")
            name1 = str(name1)
            name1 = name1.replace("\n", "")
            name_list.append(str(name1))
            if name_list.__contains__(name):
                name = input("File contains name.\n Please enter another name - ")
        break
    return name


def add_score(file, score, name):
    file_bank = open(str(file), "a")
    file_bank.write(str(score))
    file_bank.write(",")
    file_bank.write(str(name))
    file_bank.write("\n")
    file_bank.close()
    print("Done")
    return ""


# Listing the scores in a table form
def leaderboard(file):
    file = open(file, "r")
    leaderboard1 = []

    for line in file:
        # print(line)
        line = line.split(",")
        name = line[1]
        score = line[0]
        name = name.replace("\n", "")
        leaderboard1.append({"name": name, "score": int(score)})

    # Sort the leaderboard list in descending order by score
    for i in range(len(leaderboard1)):
        for j in range(i+1, len(leaderboard1)):
            if leaderboard1[j]["score"] > leaderboard1[i]["score"]:
                leaderboard1[i], leaderboard1[j] = leaderboard1[j], leaderboard1[i]

    print("_"*20, "LEADERBOARD", "_"*20, "\n")
    for x, player in enumerate(leaderboard1):
        print(str(x + 1) + ".", player["name"], player["score"])

    file.close()


def print_max_score():
    file_bank = open("Score_file", "r")
    max1 = [1, "a"]
    for score1 in file_bank:
        score1 = score1.split(",")
        score1[0] = int(score1[0])
        if score1[0] > max1[0]:
            max1[0] = score1[0]
            max1[1] = score1[1].replace("\n", "")

    print(max1[1], "got the maximum score of", max1[0])
    return ""


name2 = input("What is your name - ")
name = namechek("Score_file", name2)
your_score = askquiz(create_ques_bank())
print(add_score("Score_file", your_score, namechek("Score_file", name)))
print(leaderboard("Score_file"))
