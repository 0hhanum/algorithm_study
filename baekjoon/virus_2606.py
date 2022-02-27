"""
# BFS
import sys
from collections import defaultdict, deque

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

visited = [0 for _ in range(V + 1)]
graph = defaultdict(list)
queue = deque()
queue.append(1)
counter = 0

for edge in range(E):
    v, w = list(map(int, sys.stdin.readline().split()))
    graph[v].append(w)
    graph[w].append(v)

while queue:
    current = queue.popleft()
    if visited[current]:
        continue
    visited[current] = 1
    counter += 1
    for v in graph[current]:
        if not visited[v]:
            queue.append(v)

print(counter - 1)
"""

# Union Find

import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

root = [i for i in range(V + 1)]
rank = [0 for i in range(V + 1)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
        return find(root[x])
    else:
        return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    else:
        rank_x = rank[x]
        rank_y = rank[y]
        if rank_x < rank_y:
            root[x] = y
        else:
            root[y] = x
            if rank_x == rank_y:
                rank[x] += 1


for _ in range(E):
    v, w = list(map(int, sys.stdin.readline().split()))
    union(v, w)

for i in range(1, V + 1):  # root 최신화
    find(i)
    # 이래도 안되는 경우 있을거같음. find(1) 과 같은걸 count 하는 방법이 나아보임.
R = root[1]
print(root.count(R) - 1)
