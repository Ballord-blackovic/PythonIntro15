from random import randint

lst = [randint(10, 99) for _ in range(20)]
# print(lst)


def print_list(my_lst):
    for value in my_lst:
        print('(' + str(value) + ')', end=' ')
    print()


print_list(lst)
for i in range(len(lst)):
    lst[i] = lst[i] // 2

print_list(lst)
for i in range(len(lst)):
    lst[i] = lst[i] + 5

print_list(lst)

lst1 = [randint(10, 99) for _ in range(20)]
print_list(lst1)
"""
def func_name(param1, param2, param3):
    operator 1
    operator 2
"""


def func1(a, b):
    # print(a + b)
    return a + b


func1(3, 6)
c = func1(4, 8)
print(func1(4, 8))
d = func1(4, 8) * 6
print(d)
a = func1(c, d)
b = func1(c + 5, d * 3)
z = func1(c + 5, func1(c + 5, d * 3))
print(z)


def my_pow(num, exp=2):
    return num ** exp


print(my_pow(3, 6))
print(my_pow(4))


def func2(a1, b1, c1, f1, d1=8, e1=9, g1=7):
    print(
        'a1 =', a1,
        'b1 =', b1,
        'c1 =', c1,
        'f1 =', f1,
        'd1 =', d1,
        'e1 =', e1,
        'g1 =', g1
    )


func2(2, 5, 6, 4, 6, 6, 1)
func2(2, 5, 6, 4, 6, 6)
func2(2, 5, 6, 4, 6)
func2(2, 5, 6, 4)
# func2(2, 5, 6)
func2(g1=8, a1=0, d1=9, c1=4, f1=3, b1=5)
