"""
class ClassName:
    class_body


class ClassName(parent1, parent2, ... parentN):
    class_body


1. Большие и маленькие буквы латинского алфавита, цифры, знак подчёркивания.
2. Нельзя использовать ключевые слова.
3. Нельзя начинать с цифры.

a. snake_case_style - variables & functions
b. CamelCaseStyle - classes
"""


class Human:
    age = 25
    height = 178
    weight = 74
    phone = '345-123-56'
    address = 'Odessa'


# human1 = Human()
# human2 = Human()
# human3 = Human()
#
# print(human1.age, id(human1))
# print(human2.age, id(human2))
# print(human3.age, id(human3))
#
# human1.age = 35
# print(human1.age, id(human1))
# print(human2.age, id(human2))
# print(human3.age, id(human3))


class Point:
    type_info = 'attribute of class'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # self.type_info = 'attribute of object'

    def print_point(self):
        print('x =', self.x, 'y =', self.y)
        print('type_info =', self.type_info)

    # def print_attr_class(self):
    #     print(self.type_info)


# pt1 = Point()
# # print(dir(pt1))
# # print(dir(human1))
# # print('pt1.x =', pt1.x, 'pt1.y =', pt1.y)
# # pt2 = Point(5, 7)
# # print('pt2.x =', pt2.x, 'pt2.y =', pt2.y)
# #
# # pt1.print_point()
# # pt2.print_point()
# #
# # pt = Point()
# # print(dir(pt))
# # # print(pt.type_info)
# # # pt.print_point()
# # # print(dir(pt))
# # print(pt.type_info)
# # pt.type_info = 'test'
# # print(Point.type_info)
# # print(pt.type_info)
# pt3 = Point(4, 5)
# pt4 = Point(8, 3)
#
# pt1.print_point()
# pt3.print_point()
# pt4.print_point()
#
# pt1.x = 9
# pt1.print_point()
# pt3.print_point()
# pt4.print_point()
#
# Point.type_info = 'Test'
# pt1.print_point()
# pt3.print_point()
# pt4.print_point()


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pic1 = Point(x1, y1)
        self.pic2 = Point(x2, y2)
        self.pic3 = Point(x3, y3)


tr = Triangle(3, 4, 5, 1, 7, 4)
print(tr.pic2.x)
tr.pic3.print_point()
