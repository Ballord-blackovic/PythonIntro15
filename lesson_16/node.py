class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node

    # __str__
    # __repr__

    # def __str__(self):
    #     return f'Current value: {self.__value}'

    def __repr__(self):
        return str(self.__value)


# node = Node(4)
# print(node)
