import random

word_bank = ["python", "java", "kotlin", "javascript"]
word = random.choice(word_bank)
word = list(word)
guessed_word = ["_" for i in range(len(word))]
live = 6

while live > 0 and "_" in guessed_word:
    print(guessed_word)
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        live -= 1
        print("Oops! That letter is not in the word. You have", live, "lives left.")

if live == 0:
    print("Oops, you ran out of lives. The word was - ", word)
else:
    print("Congratulations! You guessed the word!")
    print("The word was - ", word)