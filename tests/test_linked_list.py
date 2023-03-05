import unittest
from datastruct.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_at_beginning(self):
        self.linked_list.insert_beginning(1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.head.next_node, None)

    def test_insert_at_end(self):
        self.linked_list.insert_at_end(2)
        self.assertEqual(self.linked_list.head.data, 2)
        self.assertEqual(self.linked_list.head.next_node, None)

    def test_print_ll(self):
        self.linked_list.insert_at_end(3)
        self.linked_list.insert_at_end(4)
        self.linked_list.print_ll()
        self.assertEqual(self.linked_list.head.data, 3)
        self.assertEqual(self.linked_list.head.next_node.data, 4)
