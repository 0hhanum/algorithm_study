import sys

sys.setrecursionlimit(10 ** 9)  # 재귀 제한 풀기

"""
class Tree:
    def __init__(self, nodes):
        self.root = nodes[0]
        # _left = list(filter(lambda x: x < self.root, nodes))
        # _right = list(filter(lambda x: x > self.root, nodes))

        # self.left = Tree(_left) if _left else None
        # self.right = Tree(_right) if _right else None
        _left = []
        _right = []
        for node in nodes[1:]:
            if node < self.root:
                _left.append(node)
            else:
                _right.append(node)

        self.left = Tree(_left) if _left else None
        self.right = Tree(_right) if _right else None


def go(tree):
    if tree.left:
        go(tree.left)
    if tree.right:
        go(tree.right)
    print(tree.root)


nodes = []
inputs = sys.stdin.readlines()  # 입력 값 개수 안알려줄 때 hack
for i in inputs:
    nodes.append(int(i))
tree = Tree(nodes)
go(tree)
"""


def recursion(start, end):
    if start >= end:
        return
    point = -1
    toggle = False
    for i in range(start + 1, end):
        if tree[i] > tree[start]:  # start 노드가 root
            point = i
            toggle = True
            break
    if point == start + 1 >= end:
        pass
    elif toggle:
        recursion(start + 1, point)
    else:
        recursion(start + 1, end)
    if toggle:
        recursion(point, end)
    print(tree[start])  # 후위순회


tree = []
inputs = sys.stdin.readlines()  # 입력 값 개수 안알려줄 때 hack
for i in inputs:
    tree.append(int(i))
# for i in range(9):
#     tree.append(int(sys.stdin.readline()))
recursion(0, len(tree))
