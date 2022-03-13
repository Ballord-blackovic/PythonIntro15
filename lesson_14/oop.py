class SomeClass:
    pass


# class INT:
#     def __init__(self):
#         self.x = 5


def square_method(self):
    return self.x * 2


def init(self, x):
    self.x = x


# i = INT()
# print(square_method(i))

# sc = SomeClass()
# print(dir(sc))
SomeClass.new_attr = 'TEST'
SomeClass.init = init
SomeClass.square = square_method
sc = SomeClass()
sc.init(67)
print(dir(sc))
print(sc.new_attr)
print(sc.square())
sc.one_more_attr = 123
print(dir(sc))
sc1 = SomeClass()
print(dir(sc1))


# __new__
# __del__


class Person:
    def __new__(cls, *args, **kwargs):
        print('Into method __new__')
        return super().__new__(cls)

    def __init__(self):
        print('Into method __init__')

    def __del__(self):
        print('Into method __del__')


p = Person()
del p
