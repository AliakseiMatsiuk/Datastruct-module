
class Node:
    """ Это узел """
    def __init__(self, data):
        self.data = data  # тут данные
        self.next = None # тут ссылка на следующий

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Тут добавление элемента """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node