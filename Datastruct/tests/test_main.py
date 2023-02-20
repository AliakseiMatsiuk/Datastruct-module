import unittest
from Datastruct.datastruct.main import Node, Stack

class TestNode(unittest.TestCase):
    """Тест класса Node"""

    def setUp(self) -> None:
        self.node_10 = Node(10)

    def test_Node(self):
        self.assertEqual(self.node_10.data, 10)
        self.assertEqual(self.node_10.next, None)

class TestStack(unittest.TestCase):
    """Тест класса Stack"""

    def test_Stack(self):
        self.stack = Stack()
        self.assertEqual(self.stack.top, None)

    def test_Stack_push(self):
        stack = Stack()
        self.push_ex = stack.push(None)
        self.assertEqual(self.push_ex, None)