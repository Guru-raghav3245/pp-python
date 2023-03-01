string = "Wscube@1234"
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

print("lower", lcount, "upper", ucount, "number", numcount, "special", spcount)