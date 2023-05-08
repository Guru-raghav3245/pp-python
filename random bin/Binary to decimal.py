# Binary to decimal conversion
print("     BINARY TO DECIMAL CONVERSION      ")
binary = input("Enter binary number - ")
sum = 0
i = 1
for char in range(len(binary)):
    # print(binary[char], type(binary[char]))
    # print(int(binary[char]), len(binary) - i)
    sum = sum + (int(binary[char]) * 2 ** (len(binary) - i))
    i += 1
print("The decimal number is ", sum)



