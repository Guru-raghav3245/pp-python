import random

input = (input("say Rock, Paper or Scissors - "))
y = (random.choice(['Scissors', 'Paper', 'Rock']))
print('I choose - ', y)
if input == y:
    print("it is a draw")

elif input == "Rock" and y == "Scissors":
    print("You won!!")

elif input == "Paper" and y == "Rock":
    print("You won!!")

elif input == "Scissors" and y == "Paper":
    print("You won!!")

elif input == "Rock" and y == "Paper":
    print("You lost")

elif input == "Paper" and y == "Scissors":
    print("You lost")
    
elif input == "Scissors" and y == "Rock":
    print("You lost")
