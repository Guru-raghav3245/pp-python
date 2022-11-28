
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

list_a = [2, 23, -21, 0]
print(sort(list_a))