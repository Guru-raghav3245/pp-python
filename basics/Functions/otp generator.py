import random

def OTP(digits = 6):
    start = ""
    end = ""

    for starting in range(digits):
        start = start + "1"
        end = end + "9"

    start = int(start)
    end = int(end)

    return random.randrange(start, end)

input = int(input("What is your length of your otp - "))

print("Your otp is -", OTP(input), "\nFrom ola.", "\nPlease dont share this with anyone")







