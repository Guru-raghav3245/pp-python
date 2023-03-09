import random
def password_generator(seed_word):
    special_symbol = ['!', '@', '#', '$', '*']
    word = ''
    seed_word = list(seed_word)

    seed_word[0] = seed_word[0].capitalize()
    seed_word[-1] = seed_word[-1].capitalize()

    for x in range(len(seed_word)):
        word = str(word) + str(seed_word[x])

    seed_word = word
    number = random.randrange(0, 9)
    seed_word = seed_word + random.choice(special_symbol)
    seed_word = seed_word + str(number) + str(number + 1) + str(number + 2) + str(number + 3)
    seed_word = list(seed_word)
    word = ''
    for x in range(len(seed_word)):
        word = str(word) + str(seed_word[x])

    return word

print(password_generator("water"))