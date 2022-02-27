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


# Union Find
