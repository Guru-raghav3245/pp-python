
def btod(number):
    sum = 0
    i = 1
    for char in range(len(number)):
        sum = sum + (int(number[char]) * 2 ** (len(number) - i))
        i += 1
    return sum
binary = input("What is your binary number - ")

print("Your decimal number is", btod(binary))