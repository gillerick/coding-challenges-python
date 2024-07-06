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

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete(self, data):
        # Base cases: 1. Empty linked list 2. Data to delete is in head
        if self.head is None:
            return None

        if self.head.data == data:
            self.head = self.head.next
            return data

        # 1->2->4->8
        previous = self.head
        current = self.head.next
        while previous and current:
            if current.data == data:
                previous.next = current.next
                return data
            previous = previous.next
            current = current.next
        return None

    def __str__(self):
        output = []
        current = self.head

        while current is not None:
            output.append(str(current.data))
            current = current.next

        return '->'.join(output)


def get_midpoint(numbers: LinkedList):
    slow_pointer = numbers.head
    fast_pointer = numbers.head

    while fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer.data


def create_linked_list_from_list(elements: list):
    linked_list = LinkedList()
    for element in elements:
        linked_list.append(element)
    return linked_list


class TestGetMidpoint(unittest.TestCase):
    def test_midpoint(self):
        self.assertEqual(4, get_midpoint(create_linked_list_from_list([3, 1, 4, 1, 5])))
        self.assertEqual(8, get_midpoint(create_linked_list_from_list([2, 7, 1, 8, 2, 8, 4])))
        self.assertEqual(0, get_midpoint(create_linked_list_from_list([12, 3, 0, 9, 2])))


class TestDeleteElementFromLinkedList(unittest.TestCase):
    def test_delete_element(self):
        self.assertEqual(1, create_linked_list_from_list([1, 2, 4, 8]).delete(1))
        self.assertEqual(None, create_linked_list_from_list([1, 2, 4, 8]).delete(9))
        self.assertEqual(4, create_linked_list_from_list([1, 2, 4, 8]).delete(4))


if __name__ == "__main__":
    unittest.main()
