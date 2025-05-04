import unittest


# Operations - get and put


# get - (1) fetch the desired key (2) Reorder it to the front of the cache (3) Return -1 if does not exist
# put - (1) If already exists, update else add to the cache (2) Move to the front of the cache
# LRU cache - (1) capacity static

class CacheSizeCannotBeLessThanZero(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


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
        if capacity < 0: raise CacheSizeCannotBeLessThanZero("Cache capacity cannot be less than 0")
        # Head <-> Tail

    def __len__(self):
        return len(self.cache)

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


class TestLRUCache(unittest.TestCase):

    def test_valid_initialization(self):
        lru_cache = LRUCache(4)
        self.assertEqual(0, len(lru_cache))
        self.assertEqual(4, lru_cache.capacity)
        self.assertEqual({}, lru_cache.cache)
        self.assertFalse(lru_cache.cache_is_full())

        self.assertEqual(0, lru_cache.head.key)
        self.assertEqual(0, lru_cache.head.value)
        self.assertIsNone(lru_cache.head.previous)

        self.assertEqual(0, lru_cache.tail.key)
        self.assertEqual(0, lru_cache.tail.value)
        self.assertIsNone(lru_cache.tail.next)

        self.assertIs(lru_cache.head.next, lru_cache.tail)
        self.assertIs(lru_cache.tail.previous, lru_cache.head)

    def test_invalid_initialization(self):
        with self.assertRaises(CacheSizeCannotBeLessThanZero) as ex:
            LRUCache(-2)
        expected_exception = ex.exception
        self.assertEqual("Cache capacity cannot be less than 0", expected_exception.message)

    def test_get_non_existent_key(self):
        cache = LRUCache(2)
        cache.put(1, "A")
        cache.put(2, "B")
        self.assertEqual(-1, cache.get(3))

    def test_put_and_get_single_item(self):
        cache = LRUCache(1)
        cache.put(1, "A")
        self.assertEqual("A", cache.get(1))

    def test_put_over_capacity_eviction(self):
        cache = LRUCache(2)
        cache.put(1, "A")
        cache.put(2, "B")
        self.assertEqual("A", cache.get(1))

        cache.put(3, "C")

        self.assertEqual(-1, cache.get(2))  # key 2 should have been evicted
        self.assertEqual("C", cache.get(3))  # key 2 should have been evicted
        self.assertEqual(2, len(cache))  # key 2 should have been evicted

    def test_recently_used_item_not_evicted(self):
        lru_cache = LRUCache(2)
        lru_cache.put(1, "A")
        lru_cache.put(2, "B")

        lru_cache.put(3, "C")  # key 1 should be evicted, not key 2
        self.assertEqual("B", lru_cache.get(2))
        self.assertEqual(-1, lru_cache.get(1))  # Only the least recently item was evicted

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, "A")
        cache.put(2, "B")
        cache.put(1, "A+")
        self.assertEqual("A+", cache.get(1))
