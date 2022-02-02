from random import randint

a = 9
b = 'r'

s = 'Process finished with exit code 0'
for i in range(len(s)):
    print(s[i], end=' ')
print()

for element in s:
    print(element, end=' ')
print()

############################################
s = 'Hello World!'
lst = []
print(type(lst), lst)
lst = list()
print(type(lst), lst)
lst = list(s)
print(type(lst), lst)
lst = [1, 2, 'v', True]
print(type(lst), lst)

lst = list(s)
for i in range(len(lst)):
    print(lst[i], end=' ')
print()

for element in lst:
    print(element, end=' ')
print()

print(lst[-1])
lst[-1] = '?'
print(lst)

lst[-2] = 888
print(lst)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

l4 = l1 * 3
print(l4)

s = 'Hello World!'
# len(list)
lst = list(s)
print(len(lst), lst)
print(len(s), s)

# x in lst,     x not in lst
print('o' in lst)
print('x' in lst)

print('o' not in lst)
print('x' not in lst)

# list.append(value)
lst = []
for _ in range(15):
    lst.append(randint(10, 50))
print(lst)

# min(), max(), sum()
print(min(lst))
print(max(lst))
print(sum(lst))

# list.index(value)
# print(lst.index(12))

# list.count(value)
print(lst.count(12))

# list.pop()
# list.pop(index)
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(4))
print(lst)

# list.insert(index, value)
lst.insert(4, 888)
print(lst)

# list.clear()
# lst.clear()
print(lst)

# list.extend(listN)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l1, l2, l3)
l1.extend(l2)
print(l1, l2)

# list.remove(value)
# del list[index]
l4 = [222, 444, 555, 333, 777, 888]
print(l4)
l4.remove(555)
print(l4)
del l4[3]
print(l4)

# list[::-1]
# list.revers()
print(id(lst), lst)
print(id(lst[::-1]), lst[::-1], id(lst), lst)
lst.reverse()
print(id(lst), lst)

# str.split()
# str.join(list)
s = '[31, 40, 14, 39, 50, 50, 42, 24, 22, 888, 28, 18, 30, 34]'
lst_str = s.strip('[]').split(', ')
print(lst_str)

str_res = ' + '.join(lst_str)
print(str_res, '=', eval(str_res))

lst_int = [int(value) for value in lst_str]
print(lst_int)
print(sum([int(value) for value in lst_str]))

str_line = ' - '.join([str(value) for value in lst_int])
print(str_line, '=', eval(str_line))

lst1 = []
for _ in range(15):
    lst1.append(randint(10, 50))
print(lst1)

lst2 = [randint(10, 50) for _ in range(15)]
print(lst2)

# list = [arg1 arg2]
# list = [arg1 arg2 arg3]

lst3 = [value for value in lst2 if value % 2 == 0]
print(lst3)

lst4 = [value for value in lst2 if value % 2 != 0]
print(lst4)

a = '9'
print(isinstance(a, int))

lst5 = [randint(10, 50) for _ in range(15)]
print('id lst5 =', id(lst5), 'lst5 =', lst5)

lst6 = lst5.copy()
print('id lst6 =', id(lst6), 'lst6 =', lst6)

lst5[4] = 888
print('lst5 =', lst5)
print('lst6 =', lst6)

# list.copy()
