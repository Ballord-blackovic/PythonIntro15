from random import randint
from bubble_sort import bubble

lst = [randint(10, 99) for _ in range(35)]
print(lst)


def line_search(array, key):
    for value in array:
        if value == key:
            print('Found')
            return
    print('Not found')


key = int(input('Key: '))
line_search(lst, key)


def binary_search(array, key, left=0, right=None):
    if right is None:
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key and left <= right:
        if array[middle] < key:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle+1)


bubble(lst)
print(lst)
res = binary_search(lst, key)
if res[0]:
    print(f'Key found. Index is {res[1]}')
else:
    lst.insert(res[1], key)
    print(lst)
