import this

"""
if <condition>:
    operator 1
    expression 1
else:
    operator 2
    expression 2



A  принадлежит диапазону от 10 до 50       10 <= A <= 50  ====> True
                                        A >= 10 and A <= 50
"""

a = 5

if a > 10:
    print('a > 10')
else:
    print('a < 10')

print('END')


b = -6

if b > 0:
    print('positive')
else:
    if b < 0:
        print('negative')
    else:
        print('zero')

if b > 0:
    print('positive')
elif b < 0:
    print('negative')
else:
    print('zero')

#   res = A ? B : C

c = 0

res = 'positive' if c > 0 or c == 0 else 'negative'
print(res)
