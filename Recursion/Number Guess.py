import random

def guesser(target, score = 0):
    guess = int(input("What is your guess?\nType here - "))
    if target == guess:
        congrats = ["Wow, You got it!", "Finally, you made it", "Boom! Nailed it!", "Bingo! You cracked the code!", "Bravo! Number ninja!", "Score! You hit the jackpot!", "Fantastic! You're on fire!", "Amazing! You solved the mystery!", "Hooray! Bullseye!", "Impressive! You're a guessing master!", "Yesss! You've got the magic touch!", "Incredible! You've got the gift of guessing!"]
        print(random.choice(congrats))
        print("You took - ", score, "many tries")
        return ""

    else:
        if target > guess:
            print("Guess higher!")
            score += 1
        else:
            print("Guess lower!")
            score += 1
        guesser(target)


if __name__ == "__main__":
    end1 = 100
    target = random.randrange(1, end1)
    # print(target)
    guesser(target)
