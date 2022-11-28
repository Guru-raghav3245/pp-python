def maximum(numbers):
    ans = numbers[0]
    for x in numbers:
        if x > ans:
            ans = x
    return ans




def minimum(number):
    ans = number[0]

    for x in number:

        if x < ans:
            ans = x

    return ans

list_a = [2, 23, -21, 0]
print("The min is", minimum(list_a))
print("The max is ", maximum(list_a))



