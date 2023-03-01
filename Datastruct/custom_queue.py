
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

    def dequeue(self):
        to_return = self.head.data
        if self.head is not None:
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
        return to_return

# queue = Queue()
# queue.enqueue('data1')
# queue.enqueue('data2')
# queue.enqueue('data3')
#
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())