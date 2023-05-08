def getDigitCountand0(num):
    digit_count = 0
    while True:
        num = int(num) / 10
        if num <= 0:
            break
        else:
            digit_count += 1
    return digit_count
