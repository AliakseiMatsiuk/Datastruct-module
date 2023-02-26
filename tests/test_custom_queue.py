import unittest
from datastruct.custom_queue import Node, Queue


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

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.empty_queue = Queue()
        self.data = 'data1'
        self.node = Node(self.data)

    def test_enqueue(self):
        self.empty_queue.enqueue(self.node)
        self.assertEqual(self.node.data, self.data)
