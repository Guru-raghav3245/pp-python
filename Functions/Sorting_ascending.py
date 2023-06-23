
def sort(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                ''' 
                x = list_a[i]
                list_a[i] = list_a[j]
                list_a[j] = x 
                '''
                list[i], list[j] = list[j], list[i]
    return list


qwe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0]
print(sort(qwe))