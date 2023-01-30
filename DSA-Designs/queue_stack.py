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
        pass

    def dequeue(self, element):
        """
        Remove and return the first element of the queue.
        Raise EmptyQueueException if queue is empty
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        pass

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
