def maximum(numbers):
    ans = numbers[0]
    for x in numbers:
        if x > ans:
            ans = x
    return ans
