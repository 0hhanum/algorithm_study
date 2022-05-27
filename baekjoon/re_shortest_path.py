import heapq
import sys
from collections import defaultdict

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = defaultdict(list)
distance = [float('inf') for _ in range(V + 1)]
distance[start] = 0
queue = []

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([w, v])
heapq.heappush(queue, [0, start])
while queue:
    d, node = heapq.heappop(queue)
    if d > distance[node]:
        continue
    for new_d, target in graph[node]:
        if d + new_d < distance[target]:
            distance[target] = d + new_d
            heapq.heappush(queue, [d + new_d, target])

for d in distance[1:]:
    if d == float('inf'):
        print("INF")
    else:
        print(d)
