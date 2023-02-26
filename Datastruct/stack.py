
class Node:
    """ Это узел """
    def __init__(self, data, next=None):
        self.data = data  # тут данные
        self.next_node = next # тут ссылка на следующий

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """ Тут добавление элемента """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        remove = self.top
        self.top = self.top.next_node
        return remove.data


