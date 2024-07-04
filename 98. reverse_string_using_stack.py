import unittest


class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


def reverse_string(my_string):
    stack = Stack()

    reversed_string = ""
    for char in my_string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


class TestReverseString(unittest.TestCase):
    def test_reverse_non_empty(self):
        self.assertEqual("Learn a lot with LinkedIn Learning", reverse_string("gninraeL nIdekniL htiw tol a nraeL"))

    def test_reverse_empty(self):
        self.assertEqual("", reverse_string(""))

    def test_reverse_palindrome(self):
        self.assertEqual("racecar", reverse_string("racecar"))


if __name__ == '__main__':
    unittest.main()
