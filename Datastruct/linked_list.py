class Node:
    """ Это узел """

    def __init__(self, data, next=None):
        self.data = data  # тут данные
        self.next_node = next  # тут ссылка на следующий


class LinkedList:
    """Узул для хранинея односвязного списка"""

    def __init__(self):
        self.head = None
        self.nail = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next_node
        return result

    def get_data_by_id(self, id_val):
        current = self.head
        while current is not None:
            try:
                if current.data['id'] == id_val:
                    return current.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
            current = current.next_node
        return None

ll = LinkedList()

# ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
# ll.insert_at_end('idusername')
# ll.insert_at_end([1, 2, 3])
# ll.insert_beginning({'id': 2, 'username': 'mosh_s'})
#
# user_data = ll.get_data_by_id(4)
# print(user_data)
