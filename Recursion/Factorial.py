# Factorial Program
# It is going to multiply the number with the number before that, and so on until 1
# Ex: for 3, the program should return 3*2*1, i.e. 6
#     for 6, the program should return 6*5*4*3*2*1, i.e. 720
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)  # calling the function


print(fact(6))
