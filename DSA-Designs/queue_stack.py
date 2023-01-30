class QueueStack:
    """FIFO queue implementation using list as the underlying data structure."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, element):
        """Adds element to the back of the queue"""
        pass

    def dequeue(self, element):
        """Removes and returns first element from the queue"""
        pass

    def is_empty(self):
        """Checks if the queue is empty"""
        return self.__len__() == 0

    def first(self):
        """Returns reference to the element at the front of the queue without removing it"""
        return self._data[0]
