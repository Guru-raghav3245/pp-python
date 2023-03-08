import random

# Capitalizing randomly
def password_generator(seed_word):
    special_symbol = ["`", "`", '!', '@', '#', '$', '%', '^', '&', '*', '(', ")", '-', '_', '=', '+', "[", ']', '|',
                      ';', ':', "'", '"', ',', '<', '.', '/', '?']

    seed_word = list(seed_word)
    word = ''
    for i in range(random.randrange(1, len(seed_word))):
        letter = random.choice(seed_word)
        for i in range(len(seed_word)):
            if seed_word[i] == letter:
                letter = letter.capitalize()
                seed_word[i] = letter

# Inserting numbers in random places
    for i in range(random.randrange(1, len(seed_word) - 2)):
        seed_word.insert(random.randrange(0, len(seed_word)) - 2, random.randrange(0, 10))

# Inserting special symbols
    for i in range(random.randrange(1, len(seed_word) - 2)):
        seed_word.insert(random.randrange(0, len(seed_word)) - 2, random.choice(special_symbol))

# Merging all the elements of the list
    for x in range(len(seed_word)):
        word = str(word) + str(seed_word[x])

    return word

print(password_generator("water"))