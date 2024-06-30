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
