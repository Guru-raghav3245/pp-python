num = int(input("Enter a number = "))
num2 = int(input("Enter a second number = "))
odd_even = 'odd'
sum = num + num2
if sum % 2 == 0:
    odd_even = "even"
print("{} + {} which gives {} is {}.".format(num, num2, sum, odd_even))
