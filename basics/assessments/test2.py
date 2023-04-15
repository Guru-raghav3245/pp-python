sentence = input("Please input a sentence - ")
sike = sentence.split(" ")

for n in range(len(sike)):
    if len(sike[n]) < 4:
        sike[n] = "X"

    else:
         variable = str(sike[n])
         sike[n] = variable[0:4]
print(sike)



