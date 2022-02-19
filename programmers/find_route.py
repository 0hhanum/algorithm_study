import sys

sys.setrecursionlimit(10 ** 7)


class Tree:
    def __init__(self, datas):
        self.root = max(datas, key=lambda x: x[1])
        self.index = self.root[2]
        _left = list(filter(lambda x: x[0] < self.root[0], datas))
        _right = list(filter(lambda x: x[0] > self.root[0], datas))

        if _left == []:
            self.left = None
        else:
            self.left = Tree(_left)
        if _right == []:
            self.right = None
        else:
            self.right = Tree(_right)


def go(tree, post, pre):
    post.append(tree.index)
    print(tree.root)
    if tree.left:
        go(tree.left, post, pre)
    if tree.right:
        go(tree.right, post, pre)
    pre.append(tree.index)


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    post = []
    pre = []
    tree = Tree(nodeinfo)
    go(tree, post, pre)
    return [post, pre]


# print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))

a = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
b = list(zip(range(1, len(a) + 1), a))
print(list(b))
b = sorted(b, key=lambda x: (-x[1][1], x[1][0]))
print(b)
