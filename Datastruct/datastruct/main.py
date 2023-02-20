
class Node:
    """ Это узел """
    def __init__(self, data, next=None):
        self.data = data  # тут данные
        self.next = next # тут ссылка на следующий

#node1 = Node(10)
# node2 = Node({'id': 2})
# node1.next = node2

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """ Тут добавление элемента """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

#stack = Stack()

