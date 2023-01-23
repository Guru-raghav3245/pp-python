import random
list_a = []
def OTP(digits):

    for x in range(digits):
        x = random.randrange(1, 10)
        list_a.append(x)
    return list_a






