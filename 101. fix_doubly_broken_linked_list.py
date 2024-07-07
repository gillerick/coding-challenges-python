import unittest

from adt import DoublyLinkedList


def linked_list_from_array(elements: list):
    dll = DoublyLinkedList()
    for element in elements:
        dll.append(element)

    return dll


def fix_broken_doubly_linked_list(dll: DoublyLinkedList):
    """
    Logic: A doubly linked list is broken if one of the nodes is not pointed to
    a previous or next node, so that the length of the list will be different dor forward and backward traversals
    """
    forward_nodes = []
    current = dll.head
    while current:
        forward_nodes.append(current)
        current = current.next

    backward_nodes = []
    current = dll.tail
    while current:
        backward_nodes.append(current)
        current = current.prev

    broken_backward = len(forward_nodes) > len(backward_nodes)

    if broken_backward:
        repair_nodes(forward_nodes, 1)
    else:
        repair_nodes(backward_nodes, -1)


def repair_nodes(nodes, direction: int):
    all_nodes = nodes[::direction]
    for i, node in enumerate(all_nodes):
        if i != 0:
            node.prev = all_nodes[i - 1]
        if i != len(all_nodes) - 1:
            node.next = all_nodes[i + 1]


class TestRemoveDuplicate(unittest.TestCase):
    # ToDO: Add unit tests
    def test_repair_forward_broken_nodes(self):
        pass

    def test_repair_backward_broken_nodes(self):
        pass


if __name__ == "__main__":
    unittest.main()
