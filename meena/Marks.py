marks = int(input("Enter your marks - "))

if 0 < marks <= 60:
    print("You have received the grade D")

elif 60 < marks <= 75:
    print("You have received the grade C")

elif 75 < marks <= 85:
    print("You have received the grade B")

elif 85 < marks <= 100:
    print("You have received the grade A")