def password_checker(string):
    lcount = ucount = numcount = spcount = 0
    for c in string:
        if c.isupper():
            ucount += 1
        elif c.islower():
            lcount += 1
        elif c.isdigit():
            numcount += 1
        else:
            spcount += 1
    if lcount and ucount and numcount and spcount > 0:
        print(1)
    else:
        print(0)
print(password_checker("1111111111111"))


