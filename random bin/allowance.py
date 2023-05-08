money = [20, 25, 10, 35, 20, 20, 20, 25, 20, 25, 20, 20]
spent = [15, 20, 20, 25, 15, 15, 15, 15, 15, 5, 15, 20]
month = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

most_money = max(money)
print(most_money)

min_spent = min(spent)
print(min_spent)

lis1 = [money[0] + money[1] + money[2] + money[3] + money[4] + money[5] + money[6] + money[7] + money[8] + money[9] + money[10] + money[11]]
lis2 = [spent[0] + spent[1] + spent[2] + spent[3] + spent[4] + spent[5] + spent[6] + spent[7] + spent[8] + spent[9] + spent[10] + spent[11]]
print("\n ans ", lis1[0] - lis2[0])

#for month_name in month:
    #print(month_name)

print("len of month ",len(month))
for number in range(len(month)):
       # print("In month of ", month[number],"I received rupees", money[number], "and I spent rupees", spent[number])
     if money[number] == most_money:
         print("I received maximum money in the month of", month[number] )

     if spent[number] == min_spent:
             print("I spent minimum money in the month of", month[number])



