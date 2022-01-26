"""
while <condition>:
    operator 1
    operator 2

operatorX
"""

i = 1
while i <= 10:
    print(i, end=', ')
    i += 1
print()

# break
while True:
    val = int(input('Please enter a number: '))
    if val == 0 or val == 6 or val == 23:
        break
    print(val ** 2)
print('END')

# continue
while True:
    a = int(input('Please enter first number: '))
    if a == 0:
        break
    b = int(input('Please enter second number: '))
    if b == 0:
        print('Try to divided by 0')
        continue
    print(a / b)

print('END')

# else
while val != 10:
    val = int(input('Please enter a number: '))
    if val == 0:
        break
    print(val ** 2)
else:
    print('FINISH')

print('END')
