import unittest
from datastruct.main import Node, Stack


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node1 = Node('data1')
        self.node2 = Node('data2')
        self.node1.next_node = self.node2

    def test_node_data(self):
        self.assertEqual(self.node1.data, 'data1')
        self.assertEqual(self.node2.data, 'data2')

    def test_next_node(self):
        self.assertEqual(self.node1.next_node, self.node2)

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push('data1')
        self.assertEqual(self.stack.top.data, 'data1')
        self.stack.push('data2')
        self.assertEqual(self.stack.top.data, 'data2')

    def test_pop(self):
        self.stack.push('data1')
        self.stack.push('data2')
        self.assertEqual(self.stack.pop(), 'data2')
        self.assertEqual(self.stack.pop(), 'data1')