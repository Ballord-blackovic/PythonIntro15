def div(a, b):
    # if b == 0:
    #     raise ZeroDivisionError('Param "b" is zero')
    return a / b


print(div(3, 7))
x = 4
y = 1
# print(div(x, y))

try:
    print(div(x, y))
except ZeroDivisionError:
    print('Zero errors:')
    f = ZeroDivisionError
except TypeError:
    print('Type error:')
except Exception:
    pass
else:
    print('else')
finally:
    print('finally')


assert 4 != 4, '4 != 4'

# if 4 == 4:
#     raise AssertionError('4 != 4')
