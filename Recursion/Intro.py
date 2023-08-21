def recursion(variable):
    if variable <= 900:
        print(variable)
        variable += 1
        recursion(variable)
    else:
        return ""


var = 1
recursion(var)
print('Thank you')
