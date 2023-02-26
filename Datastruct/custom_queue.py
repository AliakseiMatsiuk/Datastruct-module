class Node:
    """ Это узел """

    def __init__(self, data, next=None):
        self.data = data  # тут данные
        self.next_node = next  # тут ссылка на следующий


class Queue:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, value):
        new_node = Node(data=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


# queue = Queue()
# queue.enqueue('data1')
# queue.enqueue('data2')
# queue.enqueue('data3')
#
# print(queue.head.data)
# print(queue.head.next_node.data)
# print(queue.tail.data)
# print(queue.tail.next_node)
# print(queue.tail.next_node.data)
