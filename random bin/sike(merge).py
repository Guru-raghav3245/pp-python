# Given two sorted series of numbers in form of two lists
# merge two series
# Find the sum of the middle 2 numbers

series1 = [11, 13, 18, 19, 52]
series2 = [5, 15, 20, 25, 30, 35, 40, 45, 50]


def sort(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

series1max = sort(series1)
series2max = sort(series2)

merge = series1 + series2
print(series1max    , series2max,     merge)


def mid(list):
    x = len(list)

    int(x)
    x = x / 2
    x = int(x)
    y = x + 1
    y = int(y)


    a = list[x]
    print(a)
    b = list[y]
    print(b)

    return a + b

print(mid(merge))

"""This is the end of the file"""
