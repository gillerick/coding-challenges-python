import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def __str__(self):
        output = []

        current = self.head

        while current:
            output.append(str(current.data))
            current = current.next
        return '->'.join(output)


def linked_list_from_array(elements: list):
    linked_list = LinkedList()
    for element in elements:
        linked_list.append(element)

    return linked_list


def remove_duplicate(linked_list: LinkedList):
    current_element = linked_list.head
    next_element = current_element.next

    while next_element:
        if current_element.data == next_element.data:
            current_element.next = next_element.next
        else:
            current_element = current_element.next

    return linked_list


class TestRemoveDuplicate(unittest.TestCase):
    def test_remove_duplicate_single_element(self):
        self.assertEqual('', remove_duplicate(linked_list_from_array([2, 3, 3, 4])))


if __name__ == "__main__":
    unittest.main()
