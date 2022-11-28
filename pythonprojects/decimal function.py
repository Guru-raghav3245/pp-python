num = input("Enter decimal number - ")
ans = num
binary_num = []
last_ans = []

def dtob(number):
    ans = number
    binary_num = []
    last_ans = []
    if num.isnumeric():
            num = int(number)
            quo = int(number)
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

    else:
        print(ans, " not a decimal number")

    return binary_num
num = input("Enter decimal number - ")
print("Your decimal number is", dtob(num))