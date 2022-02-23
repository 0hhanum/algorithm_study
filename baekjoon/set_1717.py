import sys


n, m = map(int, sys.stdin.readline().split())

root = []
rank = []


def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return find(root[x])


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        root[y] = x
    else:
        root[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


for i in range(n + 1):
    root.append(i)
    rank.append(0)
for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        union(a,b)
    else:
        a = find(a)
        b = find(b)
        if a == b:
            print("YES")
        else:
            print("NO")
