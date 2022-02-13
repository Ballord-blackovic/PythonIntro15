from random import randint
# a = lambda x, y, z: x + y - z
# p = a(3, 4, 2)
# print(p)
# print((lambda x, y, z: x + y - z)(8, 6, 2))

# def far(temp):
#     return round(((float(9) / 5) * temp + 32), 2)


# def cel(temp):
#     return round((5.0 / 9) * (temp - 32), 2)


lst_in = [36.7, 35.8, 39.0, 38.1, 36.6]
# lst_out_far = []
# for t in lst_in:
#     lst_out_far.append(far(t))
# print(lst_out_far)
#
# lst_out_cel = [cel(t) for t in lst_out_far]
# print(lst_out_cel)

# map, filter, zip

m_lst_out_far = list(map(lambda x: round(((float(9) / 5) * x + 32), 2), lst_in))
print(m_lst_out_far)

m_lst_out_cel = list(map(lambda x: round((5.0 / 9) * (x - 32), 2), m_lst_out_far))
print(m_lst_out_cel)

lst_in = [randint(10, 99) for _ in range(35)]
print(lst_in)

lst_odd = []
lst_even = []

for value in lst_in:
    if value % 2 == 0:
        lst_odd.append(value)
    else:
        lst_even.append(value)

print(lst_odd)
print(lst_even)

lst1 = list(filter(lambda x: x % 2 == 0, lst_in))
print(lst1)

lst2 = list(filter(lambda x: x % 2, lst_in))
print(lst2)

lst_str = ['zero', 'one', 'two', 'three']
lst_dig = [0, 1, 2]
lst_let = ['a', 'b']
# d = {}
# for i in range(len(lst_str)):
#     d[lst_str[i]] = lst_dig[i]
# print(d)

d1 = list(zip(lst_str, lst_dig, lst_let))
print(d1)
