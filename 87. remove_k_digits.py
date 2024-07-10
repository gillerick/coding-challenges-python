import unittest

"""
This function removes k digits from a given numeric string num to create the smallest possible
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)


def remove_k_digits(num: str, k: int) -> int:
    stack = Stack()
    for char in num:
        while not stack.is_empty() and k > 0 and stack.peek() > char:
            stack.pop()
            k -= 1
        stack.push(char)
    while not stack.is_empty() and k > 0:
        stack.pop()
        k -= 1

    result = "".join(stack)
    result = result.lstrip('0')
    return 0 if not result else int(result)


class TestRemoveKDigits(unittest.TestCase):
    def test_remove_k_digits(self):
        self.assertEqual(1219, remove_k_digits("1432219", 3))
        self.assertEqual(200, remove_k_digits("10200", 1))
        self.assertEqual(0, remove_k_digits("10", 2))
        self.assertEqual(0, remove_k_digits("10", 1))


if __name__ == "__main__":
    unittest.main()
