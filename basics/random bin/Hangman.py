import random

word_bank = ["python", "programming", "computer", 'keyboard', 'mouse', 'monitor', 'software', 'hardware', 'internet',
             'website','database','algorithm','machine','learning','artificial','intelligence','graphics','encryption',
             'security','virus','engine','transmission','brake','steering','suspension','radiator','windshield',
             'ignition','banana','galaxy','zodiac','popcorn','monster','diamond','bicycle','rainbow','volcano',
             'elephant']
word = random.choice(word_bank)
word = list(word)
guessed_word = ["_" for i in range(len(word))]
live = 6

while live > 0 and "_" in guessed_word:
    print("\n", " ".join(guessed_word))
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        live += 1
        print("Good guess!")
        print("You have", live, "lives left.")
    else:
        live -= 1
        print("Oops! That letter is not in the word. You have", live, "lives left.")

if live == 0:
    print("Oops, you ran out of lives. The word was - ", "".join(word).capitalize())
else:
    print("Congratulations! You guessed the word!")
    print("The word was - ", "".join(word).capitalize())
