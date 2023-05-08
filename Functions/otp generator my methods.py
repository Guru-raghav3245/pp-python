import random
def OTP(digits):
    list_a = []
    for x in range(digits):
        x = random.randrange(1, 10)
        list_a.append(x)
    return list_a






