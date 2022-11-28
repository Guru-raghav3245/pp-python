



def sort_min(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                ''' 
                x = list_a[i]
                list_a[i] = list_a[j]
                list_a[j] = x 
                '''
                lista[i], lista[j] = lista[j], lista[i]
    return lista

list_a = [2, 23, -21, 0]
print(sort_min(list_a))


