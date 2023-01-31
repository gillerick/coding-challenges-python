class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self

        while current_node is not None:
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BST(value)
                    break

            elif value >= current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BST(value)
                    break

        return self

    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False
