sentence = input("Enter a sentence - ")
my_py_friend = sentence.split(" ")
x = 0

for n in my_py_friend:
    if len(n) >= 4:
        n = n[0:4]
        my_py_friend[x] = n


    else:
        n = "X"
    x += 1
    print(n, end=" ")
