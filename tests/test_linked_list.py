import unittest
from Datastruct.linked_list import LinkedList


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

    def test_to_list(self):
        self.assertListEqual(self.linked_list.to_list(), [])
        self.linked_list.insert_beginning('test')
        self.assertListEqual(self.linked_list.to_list(), ['test'])
        self.linked_list.insert_at_end('123')
        self.linked_list.insert_at_end(1)
        self.assertListEqual(self.linked_list.to_list(), ['test', '123', 1])

    def test_get_data_by_id(self):
        self.assertIsNone(self.linked_list.get_data_by_id(123))
        self.linked_list.insert_beginning({'id': 1, 'name': 'test'})
        self.assertIsNone(self.linked_list.get_data_by_id(123))
        self.linked_list.insert_beginning({'id': 2, 'name': 'test2'})
        self.assertEqual(self.linked_list.get_data_by_id(1), {'id': 1, 'name': 'test'})
