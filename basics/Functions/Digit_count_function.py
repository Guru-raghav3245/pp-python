def getDigitCountand0(num):
    digit_count = 0
    while num > 0:
        num = int(num / 10)
        digit_count += 1
    return digit_count