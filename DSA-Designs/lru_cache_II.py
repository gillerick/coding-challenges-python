# Operations - get and put


# get - (1) fetch the desired key (2) Reorder it to the front of the cache (3) Return -1 if does not exist
# put - (1) If already exists, update else add to the cache (2) Move to the front of the cache
# LRU cache - (1) capacity static

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


# Head <-> Node 1 <-> Node 2 <-> Node 3 <-> Tail

# Head <-> Node 1 <-> Node 2 <-> Tail

# Head <-> Node <-> Tail
# Head - Node - Tail


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # hashmap - constant time access 0(1) k, v
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head
        # Head <-> Tail

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def cache_is_full(self):
        return len(self.cache) > self.capacity

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)

            if self.cache_is_full():
                lru_node = self.tail.previous
                del self.cache[lru_node.key]
                self._remove(lru_node)

    def _remove(self, node):
        # Head <- Node -> Node 2 <-> Node 3 <-> Tail
        node.previous.next = node.next
        node.next.previous = node.previous

    def _add(self, node):
        original_head_next = self.head.next
        original_head_next.previous = node
        node.next = original_head_next
        self.head.next = node
        node.previous = self.head
