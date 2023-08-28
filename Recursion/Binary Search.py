# [1,2,3,4,5,6,7,8,9,10]
# To find 3
# The program should return 2


# Normal
def finder(lst, num):
    sorted_list = sorted(lst)
    if num in sorted_list:
        index = sorted_list.index(num)
        print(f"The element {num} is found at index {index}")
    else:
        print(f"The element {num} is not in the list")


def finder2(lst, num, index=0):
    lst.sort()
    if index >= len(lst):
        print(f"The element {num} is not in the list")
        return
    if num == lst[index]:
        print(f"The element {num} is found at index {index}")
        return
    finder2(lst, num, index + 1)


def binary_search(lst, num):
    lst.sort()
    low_index, high_index = 0, len(lst) - 1
    while low_index <= high_index:
        mid = (low_index + high_index) // 2
        if lst[mid] == num:
            print(f"The element {num} is found at index {mid}")
            return
        elif lst[mid] < num:
            low_index = mid + 1
        else:
            high_index = mid - 1

    print(f"The element {num} is not in the list")

# Recursion
def binary_search2(lst, num, low_index=0, high_index=None):
    if high_index is None:
        high_index = len(lst) - 1

    if low_index <= high_index:
        mid = (low_index + high_index) // 2
        if lst[mid] == num:
            print(f"The element {num} is found at index {mid}")
            return
        elif lst[mid] < num:
            binary_search2(lst, num, mid + 1, high_index)
        else:
            binary_search2(lst, num, low_index, mid - 1)


my_list = [5, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 59, 67, 80, 93, 103]
element_to_find = 59

finder(my_list, element_to_find)
finder2(my_list, element_to_find)
binary_search(my_list, element_to_find)
binary_search2(my_list, element_to_find)