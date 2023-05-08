cur1 = input("What currency do you want to convert from - ").capitalize()
cur2 = input("What currency do you want to convert to - ").capitalize()
amount = int(input("How much do you want to convert - "))
if cur1 == "Dollar" and cur2 == "Rupee":
    print("The convertion is", amount*80, cur2)

if cur1 == "Rupee" and cur2 == "Dollar":
    print("The convertion is", amount*0.8, cur2)

elif cur1 == "Dollar" and cur2 == "Euro":
    print("The convertion is", amount*0.9, cur2)

elif cur1 == "Euro" and cur2 == "Dollar":
    print("The convertion is", amount*1.11, cur2)