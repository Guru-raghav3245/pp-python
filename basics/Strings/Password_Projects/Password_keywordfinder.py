def password_finder(string):
    """
    special_symbol = ["`", "`", '!', '@', '#', '$', '%', '^', '&', '*', '(', ")", '-', '_', '=', '+', "[", ']', '|',
                      ';', ':', "'", '"', ',', '<', '.', '/', '?']
    string = list(string)
    word = ''
    for c in string:
        if c.isupper():
            continue
        elif c.islower():
            continue
        elif c.isdigit():
            string.remove(c)
        elif special_symbol.__contains__(c):
            string.remove(c)

    for x in range(len(string)):
        word = str(word) + str(string[x])

    word = word.capitalize()
    return word"""
    word = ''
    for i in string:
        if i.isalpha():
            word += i
    #word = word.capitalize()

    word1 = [i for i in string if i.isalpha()]

    return word, word1

print(password_finder("w12aTer3@"))



