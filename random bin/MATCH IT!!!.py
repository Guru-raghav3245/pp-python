"""What are the chances of 10 numbers and letters, when randomized, are still matched?
    My project randomizes the numbers and letters, then checks if it is matched.
"""
import random

def matching_game():
    bet = int(input("How many matches do you bet on? - "))
    number_of_matches = 0
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    score = 0

    # Limit number of matches to 10
    if bet > 10:
        bet = 10
        print("Bet limited to 10.")

    num1 = num
    letter1 = letter

    random.shuffle(num1)
    random.shuffle(letter1)

    for x in range(len(num1)):
        if letter1[x] == letter[num1[x]-1]:
            print(x, num1[x], "     ", letter1[x], "     same")
            number_of_matches += 1
        else:
            print(x, num1[x], "     ", letter1[x], "     not same")

    # Evaluate the result of the game
    if bet == number_of_matches:
        print("Way to go! You got it right")
        score += 1
        print("Score - ", score)
    else:
        print("Sorry, you lost. The actual number of matches was", number_of_matches)
        print("Score - ", score)
    return score


def play_game():
    file = open("MATCH IT!!! File", "r")
    name = input("Input name - ")
    namelist = []
    result = 0

    while True:
        for line in file:
            score, name1 = line.split(",")
            name1 = str(name1)
            name1 = name1.replace("\n", "")
            namelist.append(str(name1))
            if namelist.__contains__(name) and name.isalpha() and len(name) >= 3 and name != "" and len(name) <= 15:
                name = input("File contains name.\n Please enter another name - ")

            if name.isalpha() and len(name) >= 3 and name != "" and len(name) <= 15:
                break
            elif len(name) <= 3:
                name = input("Too less characters. \nPlease input a valid name - ")
            elif name == "":
                name = input("Please input a valid name - ")
            elif len(name) >= 15:
                name = input("Too many characters. Please input a valid name - ")
            else:
                 name = input(" Only alphabetic Characters. \nPlease input a valid name - ")
        file.close()
        break

    for i in range(5):
        result += matching_game()

    file = open("MATCH IT!!! File", "a")
    file.write(str(result))
    file.write(",")
    file.write(str(name))
    file.write("\n")
    file.close()

def leaderboard(file):
    file = open(file, "r")
    leaderboard1 = []

    for line in file:
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
        rank = str(x + 1)
        name = player["name"]
        score = player["score"]
        space = (20 - len(name)) * " "
        print(rank + ".", name, space, score)

    file.close()


if __name__ == "__main__":
    print(play_game())
    print(leaderboard("MATCH IT!!! File"))
