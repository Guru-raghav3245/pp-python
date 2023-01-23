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








