import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, data):
        current = self.head

        while current.next:
            if current.data == data:
                return data
            current = current.next
        return None


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def peek(self):
        return self.items[-1]

    def __iter__(self):
        iter(self.items)


def linked_list_from_array(elements):
    linked_list = LinkedList()
    for element in elements:
        linked_list.append(element)
    return linked_list


def is_linked_list_palindrome_fast_and_slow_runner(linked_list: LinkedList):
    fast_runner = linked_list.head
    slow_runner = linked_list.head

    stack = Stack()

    while fast_runner and fast_runner.next:
        stack.push(slow_runner.data)
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

    #     Has odd number of elements, so skip the middle element
    if fast_runner:
        slow_runner = slow_runner.next

    while slow_runner:
        if stack.pop() != slow_runner.data:
            return False
        slow_runner = slow_runner.next
    return True


class TestLinkedListPalindrome(unittest.TestCase):
    def test_linked_list_palindrome_fast_and_slow_runner_odd_elements_palindrome(self):
        self.assertEqual(True, is_linked_list_palindrome_fast_and_slow_runner(linked_list_from_array([1, 2, 3, 2, 1])))

    def test_linked_list_palindrome_fast_and_slow_runner_even_elements_palindrome(self):
        self.assertEqual(True,
                         is_linked_list_palindrome_fast_and_slow_runner(linked_list_from_array([9, 2, 2, 2, 2, 9])))

    def test_linked_list_palindrome_fast_and_slow_runner_even_elements_non_palindrome(self):
        self.assertEqual(False, is_linked_list_palindrome_fast_and_slow_runner(linked_list_from_array([1, 2])))


if __name__ == "__main__":
    unittest.main()
