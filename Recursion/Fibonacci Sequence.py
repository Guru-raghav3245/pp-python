# Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# For example, if you start with 0 and 1, It goes like 0, 1, 1, 2, 3, 5, 8, 13, and continues.
import time


def fibonacci(no_of_times,a=None, count=None):
    if count == None:
        count = 1
    if count <= no_of_times:
        if a == None:
            a = 0
        b = a + 1
        c = a + b
        time.sleep(1)
        print(a,b,c)
        fibonacci(no_of_times, a+1, count+1)


def fibonacci1(no_of_times, a=None, b=None, c=None, count=None):
    if count is None:
        count = 0
    if count < no_of_times:
        if a is None:
            a = 0
            b = 1
            print(a, b)
        else:
            c = a + b
            print(c)
            a = b
            b = c
        time.sleep(1)
        fibonacci1(no_of_times, a, b, c, count + 1)


if __name__ == "__main__":
    times = int(input("How many times do you want to repeat the program - "))
    if times < 2:
        times = int(input("Minimum is 2 - "))
    # fibonacci(times)
    fibonacci1(times)
