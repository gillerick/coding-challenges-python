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


def linked_list_from_array(elements: list):
    linked_list = LinkedList()
    for element in elements:
        linked_list.append(element)
    return linked_list


def sum_linked_lists(linked_list_one, linked_list_two):
    carry = 0
    total = 0
    place_value = 0
    node_one = linked_list_one.head
    node_two = linked_list_two.head

    while node_one or node_two or carry != 0:
        value_one = node_one.data if node_one is not None else 0
        value_two = node_two.data if node_two is not None else 0
        sum_of_values = value_one + value_two + carry

        total += (sum_of_values % 10) * (10 ** place_value)
        carry = sum_of_values // 10

        node_one = node_one.next if node_one is not None else None
        node_two = node_two.next if node_two is not None else None
        place_value += 1
    return total


class TestSumLinkedLists(unittest.TestCase):
    def test_sum_linked_lists_same_number_of_digits(self):
        list_one = linked_list_from_array([1, 2, 3])  # 321
        list_two = linked_list_from_array([1, 2, 3])  # 321
        self.assertEqual(642, sum_linked_lists(list_one, list_two))

    def test_sum_linked_lists_same_number_of_digits_with_carry(self):
        list_one = linked_list_from_array([9, 7, 5])  # 579
        list_two = linked_list_from_array([5, 9, 3])  # 395
        self.assertEqual(974, sum_linked_lists(list_one, list_two))

    def test_sum_linked_lists_different_number_of_digits_with_carry(self):
        list_one = linked_list_from_array([9, 7, 5])  # 579
        list_two = linked_list_from_array([5, 9])  # 95
        self.assertEqual(674, sum_linked_lists(list_one, list_two))


if __name__ == "__main__":
    unittest.main()
