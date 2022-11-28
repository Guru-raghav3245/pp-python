

def dtob(number):
    number = int(number)
    binary_num = []
    last_ans = []
    while True:
        quo = int(number / 2)
        rem = number % 2
        print("quotient = ", quo, "and remainder = ", rem)
        binary_num.append(rem)
        number = quo
        print(binary_num)
        if quo == 0:
            break

        for i in range(len(binary_num) - 1, -1, -1):
            last_ans.append(binary_num[i])

    return last_ans

x = int(input("Please input decimal number - "))

print("Your binary number is - ", dtob(x))


