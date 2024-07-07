from adt import LinkedList


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL(LinkedList):
    def __init__(self):
        super().__init__()
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def search(self, data):
        current = self.head

        while current.next:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete(self, data):

        node_to_delete = self.search(data)

        if not node_to_delete:
            return

        if node_to_delete == self.head:
            self.head = self.head.next

        if node_to_delete.prev:
            node_to_delete.prev.next = node_to_delete.next

        if node_to_delete.next:
            node_to_delete.next.prev = node_to_delete.prev

    def __str__(self):
        output = []
        current = self.head

        while current:
            output.append(str(current.data))
            current = current.next

        return '<-->'.join(output)


if __name__ == '__main__':
    ll = DLL()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll.head.next.data)  # 2
    print(ll.head.next.prev.data)  # 1
    print(ll)  # 1<-->2<-->3<-->4
