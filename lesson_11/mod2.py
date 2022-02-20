# import importlib
# import time
#
# import lesson_10.mod1
# import lesson_10.pak.mod_y as my_mod
#
# from lesson_10.pak import mod_y

print(dir())

from lesson_10.pak import *
from lesson_10.mod1 import *

print(dir())

# print(my_mod.func())
#
# time.sleep(3)
# importlib.reload(lesson_10.mod1)
# time.sleep(3)
# importlib.reload(lesson_10.mod1)
# time.sleep(3)
# importlib.reload(lesson_10.mod1)
# time.sleep(3)
# importlib.reload(lesson_10.mod1)
# time.sleep(3)
# importlib.reload(lesson_10.mod1)
# time.sleep(3)
# importlib.reload(lesson_10.mod1)

# import random as r0
# from random import randint as r1
# from mod_x import randint as r2
# from random import *

# print(dir())
# random.randint(12, 67)
# r2(45, 78)
# r1(45, 56)


def my_randint_func(x, y):
    from random import randint
    # from random import *
    return randint(x, y)


print(dir())
print(my_randint_func(23, 78))
print(dir())
