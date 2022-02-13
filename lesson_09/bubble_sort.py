from random import randint

# lst = [randint(10, 99) for _ in range(35)]
# print(lst)


def bubble(array):
    cnt = 0
    for i in range(len(array) - 1):
        flag = True
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False
        cnt += 1
        if flag:
            break
    # print(cnt)


# print(bubble(lst))
# print(lst)
