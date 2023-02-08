import unittest

from adt import LinkedList


def remove_duplicates_from_linked_list(head: LinkedList = None):
    if not head:
        return None

    seen = set()
    seen.add(head.data)
    prev = head
    current = head.next
    while current:  # Same as while current is not None
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            # Moves starting (head) node to the next node
            prev = current
        # Moves current node a step forward (head.next.next)
        current = current.next
    return head


class TestDeleteLinkedListDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        result = remove_duplicates_from_linked_list(LinkedList(2, LinkedList(4, LinkedList(7, LinkedList(2)))))
        self.assertEqual(2, result.data)
        self.assertEqual(4, result.next.data)
        self.assertEqual(7, result.next.next.data)
        self.assertEqual(None, result.next.next.next)

    def test_remove_duplicates_empty_head(self):
        self.assertEqual(None, remove_duplicates_from_linked_list(None))

    def test_remove_duplicates_from_single_node_list(self):
        result = remove_duplicates_from_linked_list(LinkedList(2))
        self.assertEqual(2, result.data)


if __name__ == "__main__":
    unittest.main()
