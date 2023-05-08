import random

def OTP(digits):
    start = ""
    end = ""

    for starting in range(digits):
        start = start + "1"
        end = end + "9"

    start = int(start)
    end = int(end)

    return random.randrange(start, end)

print(OTP(2))






