import unittest

"""
Singly linked list
O(max(n,m)) time | O(max(n,m)) time
"""


class LinkedList:
    def __init__(self, value, n=None):
        self.value = value
        self.next = n


def sum_of_linked_list(linked_list_one: LinkedList, linked_list_two: LinkedList):
    new_linked_list_head_pointer = LinkedList(0)
    current_node = new_linked_list_head_pointer
    carry = 0

    node_one = linked_list_one
    node_two = linked_list_two

    while node_one is not None or node_two is not None or carry != 0:
        value_one = node_one.value if node_one is not None else 0
        value_two = node_two.value if node_two is not None else 0
        sum_of_values = value_one + value_two + carry

        new_value = sum_of_values % 10
        new_node = LinkedList(new_value)
        current_node.next = new_node
        current_node = new_node

        carry = sum_of_values // 10
        node_one = node_one.next if node_one is not None else None
        node_two = node_two.next if node_two is not None else None

    return new_linked_list_head_pointer.next


class TestSumOfLinkedList(unittest.TestCase):
    def test_sum_of_linked_list(self):
        linked_list_one = LinkedList(2, LinkedList(4, LinkedList(7, LinkedList(1))))
        linked_list_two = LinkedList(9, LinkedList(4, LinkedList(5)))
        results = sum_of_linked_list(linked_list_one, linked_list_two)
        self.assertEqual(1, results.value)
        self.assertEqual(9, results.next.value)
        self.assertEqual(2, results.next.next.value)
        self.assertEqual(2, results.next.next.next.value)


if __name__ == "__main__":
    unittest.main()
