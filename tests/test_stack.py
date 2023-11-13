"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack

class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        stack.pop()
        self.assertEqual(stack.top.data, 'data2')
        stack.pop()
        self.assertEqual(stack.top.data, 'data1')

if __name__ == '__main__':
    unittest.main()