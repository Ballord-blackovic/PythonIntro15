from random import randint

s = {}
print(type(s), s)
s = set()
print(type(s), s)
s = {4, 6, 8, 5, 4}
print(type(s), s)
s = set('Hello World!')
print(type(s), s)

for element in s:
    print(element, end=' ')
print()

s.add('h')
print(type(s), s)

s1 = {32, 40, 41, 10, 43, 12, 13, 11, 15, 48, 17, 24, 25, 27, 29}
s2 = {39, 41, 16, 49, 18, 17, 22, 23, 24, 27, 28, 29, 31}
print(s1)
print(s2)

"""
s1.add(value)
s1.pop()
s1.remove(value)
s1.discard(value)
s1.copy()
s1.clear()
"""

# C = A | B            C = A.union(B)
# A |= B               A.update(B)

s3 = s1 | s2
print(s3)

# C = A & B             C = A.intersection(B)
# A &= B                A.intersection_update(B)

s3 = s1 & s2
print(s3)

# C = A - B             C = A.difference(B)
# A -= B                A.difference_update(B)

s3 = s1 - s2
print(s3)

# C = A ^ B             C = A.symmetric_difference(B)
# A ^= B                A.symmetric_difference_update(B)

s3 = s1 ^ s2
print(s3)

s5 = s1 - s2
s6 = s2 - s1
s7 = s5 | s6
print(s7)


lst = [chr(randint(0, 255)) for _ in range(200)]
print(len(lst), lst)
s8 = set(lst)
print(len(s8), s8)
lst1 = list(s8)
print(len(lst1), lst1)

lst2 = []
for element in lst:
    if element in lst2:
        continue
    lst2.append(element)
print(len(lst2), lst2)

#     0   1   2   3   4   5   6
l1 = [41, 17, 17, 24, 24, 27, 29]
#    [41, 17, 24, 27, 29]

fs = frozenset(l1)
print(type(fs), fs)
