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


def remove_duplicates_hash_map(linked_list: LinkedList):
    if linked_list.head is None:
        return linked_list

    seen = {}
    current = linked_list.head
    previous = None

    while current is not None:
        if current.data in seen:
            previous.next = current.next
        else:
            seen[current.data] = True
            previous = current
        current = current.next

    return linked_list


class TestRemoveDuplicate(unittest.TestCase):
    def test_remove_duplicates_hash_map_single_element(self):
        self.assertEqual('2->3->4', str(remove_duplicates_hash_map(linked_list_from_array([2, 3, 3, 4]))))

    def test_remove_duplicates_hash_map_multiple_elements(self):
        self.assertEqual('2->3->4->5',
                         str(remove_duplicates_hash_map(linked_list_from_array([2, 3, 3, 4, 4, 4, 5, 5]))))

    def test_remove_duplicates_hash_map_multiple_elements_unordered(self):
        self.assertEqual('2->3->4->5',
                         str(remove_duplicates_hash_map(linked_list_from_array([2, 3, 4, 4, 4, 5, 5, 3, 4, 5, 2]))))

    def test_remove_duplicates_hash_map_empty_linked_list(self):
        self.assertEqual('',
                         str(remove_duplicates_hash_map(linked_list_from_array([]))))


if __name__ == "__main__":
    unittest.main()
