from random import randint
from lesson_09.bubble_sort import bubble


def qsort(nums, first_idx, last_idx):
    if first_idx >= last_idx:
        return

    i, j = first_idx, last_idx
    middle = nums[(first_idx + last_idx) // 2]

    while i <= j:
        while nums[i] < middle:
            i += 1
        while nums[j] > middle:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j-1

    qsort(nums, first_idx, j)
    qsort(nums, i, last_idx)


lst = [randint(1000, 9999) for _ in range(30000)]
lst1 = lst.copy()
print(lst)
qsort(lst, 0, len(lst)-1)
# qsort(lst, 6, 23)
print(lst)
bubble(lst1)
print(lst1)
