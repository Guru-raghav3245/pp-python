import random
number = 0
check = []
numbers_list = [111, 225, 335, 445, 577, 699, 777, 881, 911]
tries = 0
tries_list = []
sum = 0

while len(check) != len(numbers_list):
    number = random.randrange(100, 1000)
    print(number)
    tries += 1
    if numbers_list.__contains__(number):
        if check.__contains__(number):
           print("Already found")
        else:
            print("found")
            tries_list.append(tries)
            sum = sum + tries
            tries = 0
            check.append(number)

print("The numbers", numbers_list)
print("The number we got", check)
print("The tries", tries_list)
for i in range(len(check)):
    print("You took", tries_list[i], "tries to get the number", check[i])
print("The total number of tries to get all 9 numbers is ", sum)
check.sort()
