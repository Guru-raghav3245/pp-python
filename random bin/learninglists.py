

our_cool_kids = ["Ananya", "Aditi", "Arnav", "Guru"]
print(our_cool_kids)

print(our_cool_kids[0])
print(our_cool_kids[3])

our_cool_kids.append("Another Cool kid")
print("The length", len(our_cool_kids))

fav_color_list = []
print(fav_color_list, "\nType of list", type(fav_color_list))
print("The length", len(fav_color_list))
for kids_name in our_cool_kids:
    print("Hello", kids_name)
    favcolor = input("What is your favorite color?")
    fav_color_list.append(favcolor)

print(fav_color_list)

