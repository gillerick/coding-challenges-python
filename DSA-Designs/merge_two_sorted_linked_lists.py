import unittest


# https://www.youtube.com/watch?v=E5XXiY6QnAs&embeds_referring_euri=https%3A%2F%2Fleetcode.com%2F&source_ve_path=OTY3MTQ&feature=emb_imp_woyt

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoLists(object):
    @staticmethod
    def merge_two_lists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return head.next


def list_to_nodes(lst):
    """ Helper function to convert list to ListNode chain. """
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def nodes_to_list(node):
    """ Helper function to convert ListNode chain to list. """
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


class TestMergeTwoLists(unittest.TestCase):
    def test_merge_two_empty_lists(self):
        l1 = None
        l2 = None
        result = MergeTwoLists.merge_two_lists(l1, l2)
        self.assertIsNone(result)

    def test_merge_one_empty_list(self):
        l1 = list_to_nodes([1, 3, 5])
        l2 = None
        expected = [1, 3, 5]
        result = MergeTwoLists.merge_two_lists(l1, l2)
        self.assertEqual(nodes_to_list(result), expected)

        l1 = None
        l2 = list_to_nodes([2, 4, 6])
        expected = [2, 4, 6]
        result = MergeTwoLists.merge_two_lists(l1, l2)
        self.assertEqual(nodes_to_list(result), expected)

    def test_merge_two_non_empty_lists(self):
        l1 = list_to_nodes([1, 2, 4])
        l2 = list_to_nodes([1, 3, 4])
        expected = [1, 1, 2, 3, 4, 4]
        result = MergeTwoLists.merge_two_lists(l1, l2)
        self.assertEqual(nodes_to_list(result), expected)

        l1 = list_to_nodes([5, 6, 7])
        l2 = list_to_nodes([1, 2, 3])
        expected = [1, 2, 3, 5, 6, 7]
        result = MergeTwoLists.merge_two_lists(l1, l2)
        self.assertEqual(nodes_to_list(result), expected)

    def test_merge_lists_with_duplicates(self):
        l1 = list_to_nodes([1, 3, 5])
        l2 = list_to_nodes([1, 3, 5])
        expected = [1, 1, 3, 3, 5, 5]
        result = MergeTwoLists.merge_two_lists(l1, l2)
        self.assertEqual(nodes_to_list(result), expected)

    def test_merge_differently_sized_lists(self):
        l1 = list_to_nodes([1, 3, 5])
        l2 = list_to_nodes([2, 4])
        expected = [1, 2, 3, 4, 5]
        result = MergeTwoLists.merge_two_lists(l1, l2)
        self.assertEqual(nodes_to_list(result), expected)

        l1 = list_to_nodes([1])
        l2 = list_to_nodes([2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        result = MergeTwoLists.merge_two_lists(l1, l2)
        self.assertEqual(nodes_to_list(result), expected)


if __name__ == '__main__':
    unittest.main()
