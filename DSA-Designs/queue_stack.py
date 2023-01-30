class EmptyQueueException(Exception):
    pass


class QueueStack:
    """FIFO queue implementation using list as the underlying data structure."""

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * QueueStack.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def enqueue(self, element):
        """Adds element to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the size of the array
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1

    def dequeue(self):
        """
        Remove and return the first element of the queue.
        Raise EmptyQueueException if queue is empty
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """
        Returns reference to the element at the front of the queue without removing it.
        Raise EmptyQueueException if queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self._data[self._front]

    def _resize(self, capacity):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * capacity  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # realign front
