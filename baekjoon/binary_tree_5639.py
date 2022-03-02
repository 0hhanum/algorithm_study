import sys

sys.setrecursionlimit(10 ** 7)  # 재귀 제한 풀기

class Tree:
    def __init__(self, nodes):
        self.root = nodes[0]
        # _left = list(filter(lambda x: x < self.root, nodes))
        # _right = list(filter(lambda x: x > self.root, nodes))

        # self.left = Tree(_left) if _left else None
        # self.right = Tree(_right) if _right else None
        _left = []
        _right = []
        index = -1
        for index, node in enumerate(nodes[1:]):
            if node > self.root:
                break

        _left = nodes[1:index + 1]
        _right = nodes[index + 1:]
        self.left = Tree(_left) if _left and index != -1 else None
        self.right = Tree(_right) if _right and index != -1 else None


def go(tree):
    if tree.left:
        go(tree.left)
    if tree.right:
        go(tree.right)
    print(tree.root)


nodes = []
# inputs = sys.stdin.readlines()  # 입력 값 개수 안알려줄 때 hack
# for i in inputs:
#     nodes.append(int(i))
for i in range(9):
    nodes.append(int(sys.stdin.readline()))
tree = Tree(nodes)
go(tree)
