"""
for variable in iter_obj:
    operator1
    operator2

for _ in iter_obj:
    operator1
    operator2
"""

# 'Hello World!'
# [4, 6, 2, 7]
# range(3, 6, 2)


for letter in 'Process finished with exit code 0':
    print(letter, end=' ')
print()

# range(start, stop, step)  ==>  start to stop range(1, 5, 2) ==> 1, 3,
# range(start, stop)    ===> range(start, stop, 1)
# range(stop)   ===>  range(0, stop, 1)

# range(1, 20, 2) ==> 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
for i in range(1, 20, 2):
    print(i, end=', ')
print()

for i in range(20):
    print(i, end=', ')
print()

for _ in range(6):
    print('Test', end=' ')
print()

num = int(input('Enter a number (0 - 65535): '))
mask = 1
res_str = ''
#                       101011101010101
#                       000000000000001
for shift in range(16):
    res = num & (mask << shift)
    res_str = str(int(bool(res))) + res_str

print(res_str)
