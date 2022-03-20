from lesson_16.node import Node
from random import randint


class SingleLinkedList:
    # def __new__
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:       # nodes == None
            copy_lst = nodes.copy()
            node = Node(value=copy_lst.pop(0))
            self.head = node
            for element in copy_lst:
                node.next = Node(value=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = ['Head']
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append('None')

        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_to_head(self, value):
        node = Node(value=value)
        node.next = self.head
        self.head = node

    def add_to_tail(self, value):
        node = Node(value=value)
        if self.head is None:
            self.head = node
            return

        current_node = None
        for current_node in self:
            pass

        current_node.next = node

    def insert_after(self, target_value, new_value):
        if self.head is None:
            raise Exception('List is empty')

        new_node = Node(value=new_value)
        for node in self:
            if node.value == target_value:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f'Node with value {target_value} not found')

    def insert_before(self, target_value, new_value):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.value == target_value:
            self.add_to_head(new_value)
            return

        new_node = Node(value=new_value)
        prev_node = self.head
        for node in self:
            if node.value == target_value:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with value {target_value} not found')

    def insert_by_number_after(self, element_number, new_value):
        if self.head is None:
            raise Exception('List is empty')

        raise Exception(f'Node with number {element_number} not found')

    def insert_by_number_before(self, element_number, new_value):
        if self.head is None:
            raise Exception('List is empty')

        raise Exception(f'Node with number {element_number} not found')

    def remove_by_value(self, target_value):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.value == target_value:
            new_head = self.head.next
            del self.head
            self.head = new_head
            # self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.value == target_value:
                prev_node.next = node.next
                del node
                return
            prev_node = node

        raise Exception(f'Node with value {target_value} not found')

    def remove_by_number(self, element_number):
        if self.head is None:
            raise Exception('List is empty')


single_list_1 = SingleLinkedList()
print(single_list_1)
# single_list_1.insert_after(34, 56)

single_list_1.add_to_tail(5)
print(single_list_1)
single_list_1.add_to_tail(15)
print(single_list_1)


single_list_2 = SingleLinkedList([randint(10, 99) for _ in range(10)])
print(single_list_2)
for element in single_list_2:
    print(element, end=' ')
print()
single_list_2.add_to_head(0)
print(single_list_2)
single_list_2.add_to_tail(1)
print(single_list_2)
# value = int(input('Please enter target value: '))
# single_list_2.insert_after(value, 4)
# print(single_list_2)
# single_list_2.insert_before(0, 8)
# print(single_list_2)
# value = int(input('Please enter target value: '))
# single_list_2.insert_before(value, 7)
# print(single_list_2)
value = int(input('Please enter target value: '))
single_list_2.remove_by_value(value)
print(single_list_2)
value = int(input('Please enter target value: '))
single_list_2.remove_by_value(value)
print(single_list_2)
