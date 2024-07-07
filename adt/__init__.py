class BST:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.left = left
        self.right = right


class LinkedList:
    def __init__(self):
        self.head = None


class DoublyLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
