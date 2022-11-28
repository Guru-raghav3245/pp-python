import random

def rps_choice(choice1, choice2):

    if choice1 == "Rock" or "Paper" or "Scissors" and choice1 == "Rock" or "Paper" or "Scissors":
        if choice1 == choice2:
            return "it is a draw"

        elif choice1 == "Rock" and choice2 == "Scissors":
            return "You won!!"

        elif choice1 == "Paper" and choice2 == "Rock":
            return "You won!!"

        elif choice1 == "Scissors" and choice2 == "Paper":
            return "You won!!"

        elif choice1 == "Rock" and choice2 == "Paper":
            return "You lost"

        elif choice1 == "Paper" and choice2 == "Scissors":
            return "You lost"

        elif choice1 == "Scissors" and choice2 == "Rock":
            return "You lost"
        else:
            return "YOU LOST"


player1_select = random.choice(["rock", "paper", "scissors"])

player2_select = random.choice(["rock", "paper", "scissors"])

print("player1 selection is:", player1_select)

print("player2 selection is:", player2_select)

result = rps_choice(player1_select, player2_select)
