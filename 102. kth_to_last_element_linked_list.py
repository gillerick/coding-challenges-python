"""
Implement an algorithm to return the Kth to last element of a singly linked list
"""
import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
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


def find_kth_to_last_element(linked_list: LL, n: int):
    slow_pointer = linked_list.head
    fast_pointer = linked_list.head

    fast_pointer = move_fast_pointer(n, fast_pointer)
    while fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer.data


def move_fast_pointer(n, node):
    for i in range(1, n):
        node = node.next
    return node


def linked_list_from_array(elements: list):
    linked_list = LL()
    for element in elements:
        linked_list.append(element)
    return linked_list


class TestFindKthToLastElement(unittest.TestCase):
    def test_find_kth_to_last_element_second_to_last(self):
        self.assertEqual(4, find_kth_to_last_element(linked_list_from_array([1, 2, 3, 4, 5]), 2))  # Second to last item

    def test_find_kth_to_last_element_third_to_last(self):
        self.assertEqual(3, find_kth_to_last_element(linked_list_from_array([1, 2, 3, 4, 5]), 3))  # Third to last item

    def test_find_kth_to_last_element_last(self):
        self.assertEqual(5, find_kth_to_last_element(linked_list_from_array([1, 2, 3, 4, 5]), 1))  # Last item


if __name__ == "__main__":
    unittest.main()
