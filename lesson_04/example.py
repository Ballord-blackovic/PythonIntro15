"""
Даны два целых числа A и В, A > B. Выведите все нечётные числа от A до B включительно,
в порядке убывания. В этой задаче можно обойтись без инструкции if.
"""

a = int(input('A: '))
b = int(input('B: '))
#                24 + 0 - 1
for i in range(a + (a % 2) - 1, b - 1, -2):
    print(i, end=', ')
print()
