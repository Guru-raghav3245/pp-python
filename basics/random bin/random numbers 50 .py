import random
number = 0
i = 0
tries = 0
count = []

for i in range(10):
    while number != 50:
        number = random.randrange(1, 100)
        tries += 1
        print(number)
        if number > 50:
            print("Go down")

        elif number < 50:
            print("go up")

        else:
            print("You have hit the Jackpot in", tries, "tries")
            number = 0
            count.append(tries)
            if tries < 5:
                print("MEGA JACKPOT!!!!, look at the number of tries!!!!", tries)
            tries = 0
            break
print("count:", count)

print(max(count), "is the most number of times is took u to get 50")
print(min(count), "is the least number of times is took u to get 50")

