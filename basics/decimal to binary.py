num = input("Enter decimal number - ")
ans = num
binary_num = []
last_ans = []

if num.isnumeric():
        num = int(num)
        quo = int(num)
        while True:
            quo = int(num / 2)
            rem = num % 2
            print("quotient = ", quo, "and remainder = ", rem)
            binary_num.append(rem)
            num = quo
            print(binary_num)
            if quo == 0:
                break

        for i in range(len(binary_num) - 1, -1, -1):
            last_ans.append(binary_num[i])

        print(ans, "is converted as a binary number to", last_ans)

else:
    print(ans, " not a decimal number")


