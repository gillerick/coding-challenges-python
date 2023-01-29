"""All the nodes are also known as vertices
Time complexity - O(V+E) |  Space complexity - O(V)
We are adding a bunch of frames on the call stack for each of the calls on the BFS for each of the vertices(V)
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array
