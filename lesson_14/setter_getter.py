# property(get, set, del, comment)

# _PositivePoint__x
class PositivePoint:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __set_x(self, x):
        print('Setter X')
        if x < 0:
            self.__x = -x
        else:
            self.__x = x

    def __get_x(self):
        print('Getter X')
        return self.__x

    def __del_x(self):
        print('Deleter X')
        self.__x = None

    def __set_y(self, y):
        if y < 0:
            self.__y = -y
        else:
            self.__y = y

    def __get_y(self):
        return self.__y

    def __del_y(self):
        self.__y = None

    x = property(__get_x, __set_x, __del_x, 'Property for attribute X')
    y = property(__get_y, __set_y, __del_y, 'Property for attribute Y')


p1 = PositivePoint(4, 5)
# p1.set_x(-9)
# print(p1.get_x())
# p1.x = 40

p1.x = -5
print(p1.x)
del p1.x
print(p1.x)
