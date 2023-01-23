def minimum(number):
    ans = number[0]
    for x in number:
        if x < ans:
            ans = x
    return ans