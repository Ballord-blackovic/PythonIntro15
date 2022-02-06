from random import randint

lst = []
for i in range(15):
    res = (randint(10, 50) // 25 + 18) ** 2
    lst.append(randint(10, 50))
print(lst)
