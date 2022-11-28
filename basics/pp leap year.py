print("leap year")
list_a = []
for year in range(2000, 3000, 1):
    if year % 400 == 0:
        print(year)
    else:
        if year % 100 != 0:
            if year % 4 == 0:
               list_a.append(year)
print(list_a)
rec = 0
for rec in range(len(list_a)-4):

    if rec / 5 == 0:
        print("\n")

    else:
         if rec > len(list_a):
             exit()
         else:
          if rec == len(list_a) or rec == len(list_a) - 1 or rec == len(list_a) - 2 or rec == len(list_a) - 3 or rec == len(list_a) - 3:
              exit()
          else:
              print(list_a[rec - 1], list_a[rec], list_a[rec + 1], list_a[rec + 2], list_a[rec + 3])
              rec = rec + 5










