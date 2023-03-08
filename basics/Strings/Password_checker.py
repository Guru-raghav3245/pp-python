def password_checker(string):
    lcount = ucount = numcount = spcount = 0
    for c in string:
        if len(string) >= 8:
            if c.isupper():
                ucount += 1
            elif c.islower():
                lcount += 1
            elif c.isdigit():
                numcount += 1
            else:
                spcount += 1
        else:
            return 0

    if lcount and ucount and numcount and spcount > 0:
        return 1
    else:
        return 0

print(password_checker("Water^12"))



