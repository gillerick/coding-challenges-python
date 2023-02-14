import unittest

"""
Singly linked list
O(max(n,m)) time | O(max(n,m)) time
"""


class LinkedList:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


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


def sum_of_linked_list_reversal_technique(linked_list_one, linked_list_two):
    linked_list_one = reverse_linked_list(linked_list_one)
    linked_list_two = reverse_linked_list(linked_list_two)

    dummy_head = LinkedList(0)
    current = dummy_head
    carry = 0

    while linked_list_one or linked_list_two:
        x = linked_list_one.val if linked_list_one else 0
        y = linked_list_two.val if linked_list_two else 0
        total = carry + x + y
        carry = total // 10
        current.next = LinkedList(total % 10)
        current = current.next
        if linked_list_one:
            linked_list_one = linked_list_one.next
        if linked_list_two:
            linked_list_two = linked_list_two.next

    if carry > 0:
        current.next = LinkedList(carry)

    return reverse_linked_list(dummy_head.next)


def reverse_linked_list(head_node):
    previous_node = None
    current_node = head_node

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


class TestSumOfLinkedList(unittest.TestCase):
    def test_sum_of_linked_list(self):
        linked_list_one = LinkedList(2, LinkedList(4, LinkedList(7, LinkedList(1))))
        linked_list_two = LinkedList(9, LinkedList(4, LinkedList(5)))
        results = sum_of_linked_list(linked_list_one, linked_list_two)
        self.assertEqual(1, results.value)
        self.assertEqual(9, results.next.value)
        self.assertEqual(2, results.next.next.value)
        self.assertEqual(2, results.next.next.next.value)

    def _test_sum_of_linked_list_reversal_technique(self):
        linked_list_one = LinkedList(2, LinkedList(3, LinkedList(7, LinkedList(1))))
        linked_list_two = LinkedList(9, LinkedList(3, LinkedList(5)))
        results = sum_of_linked_list_reversal_technique(linked_list_one, linked_list_two)
        self.assertEqual(1, results.value)
        self.assertEqual(7, results.next.value)
        self.assertEqual(2, results.next.next.value)
        self.assertEqual(2, results.next.next.next.value)


if __name__ == "__main__":
    unittest.main()
