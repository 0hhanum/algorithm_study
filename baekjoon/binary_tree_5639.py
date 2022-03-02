import sys


class Tree:
    def __init__(self, nodes):
        self.root = nodes[0]
        _left = list(filter(lambda x: x < self.root, nodes))
        _right = list(filter(lambda x: x > self.root, nodes))

        self.left = Tree(_left) if _left else None
        self.right = Tree(_right) if _right else None


def go(tree):
    if tree.left:
        go(tree.left)
    if tree.right:
        go(tree.right)
    print(tree.root)


nodes = []
inputs = sys.stdin.readlines()
for i in inputs:
    nodes.append(int(i))
tree = Tree(nodes)
go(tree)
