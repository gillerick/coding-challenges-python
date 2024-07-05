class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def __str__(self):
        output = []
        current = self.head

        while current:
            output.append(str(current.data))
            current = current.next

        return '->'.join(output)


if __name__ == '__main__':
    ll = LL()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll)  # 1->2->3->4
