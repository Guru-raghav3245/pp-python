# Input = 671 output = 14(adding all digits in given number)

num = input("Input a number - ")
num_list = []
sum = 0

for char in num:
    num_list.append(char)

for i in range(len(num_list)):
    sum = sum + int(num_list[i])
print(sum)
