sentence = input("tell me your sentence - ")

words = []
words = sentence.split(" ")
print(words)


if len(words) < 5:
    print("dont be lazy, this is only", len(words), "words")

else:
    words[0] = "b" + words[0]
    words[2] = "b" + words[2]

    x = len(words)

    words[x - 1] = "z" + words[x - 1]
    print(words)







