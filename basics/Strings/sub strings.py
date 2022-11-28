word = input("Input word - ")
length = (len(word))
sub_strings = []
print(word[0])

for start in range(len(word) + 1):
    for end in range(start, len(word) + 1, 1):
        print(start, end)
        sub_strings.append(word[start:end])
print(sub_strings)










