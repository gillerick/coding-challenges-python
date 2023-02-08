class BST:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.left = left
        self.right = right


class LinkedList:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next
