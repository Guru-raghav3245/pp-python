sentence = input("Please input a sentence - ")
my_py_friend = sentence.split(" ")

for n in range(len(my_py_friend)):
    if len(my_py_friend[n]) < 4:
        my_py_friend[n] = "X"

    else:
         variable = str(my_py_friend[n])
         my_py_friend[n] = variable[0:4]
print(my_py_friend)
