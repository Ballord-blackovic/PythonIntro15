from random import randint

tup = ()
print(type(tup), tup)
tup = tuple()
print(type(tup), tup)
tup1 = tuple('Hello World!')
print(type(tup1), tup1)
tup2 = tuple([34, 65, 97, 23, 11])
print(type(tup2), tup2)
tup3 = (34, 'TEST', True, 0.15)
print(type(tup3), tup3)

# const int a = 89;
# final int b = 34;

t = (9.8, 3.14)
print(t[0])
print(t[1])


def func1():
    w = 45
    v = 56
    return w + v, w * v


res = func1()
a, b = res
x, y = func1()

t = 30,
print(t, len(t))

t = 30, 56, 'TEST', True
print(type(t), t)

lst = [7]
print(type(lst), lst)

"""
len(tuple)
tuple3 = tuple1 + tuple2
new_tuple = tuple * int
value in tuple 
value not in tuple
tuple.index(value, start, end)
tuple.count(value)
max(tuple)
min(tuple)
sum(tuple)
"""

tup = tuple(randint(10, 50) for _ in range(15))
print(type(tup), tup)
for value in tup:
    print(value, end=' ')
print()

for idx in range(len(tup)):
    print(tup[idx], end=' ')
print()

