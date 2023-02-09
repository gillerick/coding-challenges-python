"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key: int) -> int:
        """
        The get method first checks if the key exists in the cache. If it does, it removes the node associated with
        the key from its current position in the linked list and adds it to the front of the list. This updates the
        order of the elements in the list to reflect the most recent use of the key. Finally, the value associated
        with the key is returned. If the key does not exist in the cache, the method returns -1.

        :param key:
        :return: key or -1
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return key
        return -1

    def put(self, key: int, value: int) -> None:
        """
        The put method first checks if the key exists in the cache. If it does, the associated node is removed from
        its current position in the linked list. Then, a new node is created and added to the front of the list,
        and the key-value pair is added to the hash map. Finally, if the size of the cache is greater than its
        capacity, the least recently used node (the node at the end of the linked list) is removed from both the
        linked list and the hash map.

        :param key:
        :param value:
        """
        pass

    def _remove(self, node: Node):
        """
        The _remove method is used to remove a node from the doubly linked list.

        The method takes in a node as an argument, and updates the pointers of the neighboring nodes to effectively
        remove node from the list.

        (1) Update the next pointer of the previous node to point to the next node: node.prev.next = node.next
        (2) Update the prev pointer of the next node to point to the previous node: node.next.prev = node.prev

        By updating the pointers in this way, we effectively disconnect the node from the rest of the list,
        so it is no longer accessible. The node will eventually be garbage collected by the Python interpreter.

        :param node:
        """
        node.previous.next = node.next
        node.next.previous = node.previous

    def _add(self, node):
        node.previous = self.head
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node
