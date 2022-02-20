"""
Some information

"""

# import module_name
import sys
from random import randint

__all__ = ['string', 'num']

string = 'Hello World'
num = 63454546
pi = 3.14

some_lst = [1, 2, 3, 'Test']


def print_lst(lst):
    """
    Information about this function

    Extra information
    :param lst: input value
    :return:
    """
    for el in lst:
        print(el, end=' ')
    print()

# PYTHONPATH


# print(sys.path)
# print(randint(10, 56))
# print(__name__, 3, 547, 'df')
if __name__ == '__main__':
    print(__name__)
    print(randint(34, 78))
    print(dir())
    print(sys.path)
