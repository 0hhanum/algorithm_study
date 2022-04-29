import heapq
import sys
from collections import defaultdict

V, E = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append([w, b])
    graph[b].append([w, a])

connected = [0 for _ in range(V + 1)]
connected[1] = 1
candidate = graph[1]
heapq.heapify(candidate)
answer = 0

while candidate:
    w, node = heapq.heappop(candidate)
    if not connected[node]:
        answer += w
        connected[node] = 1
        for connection in graph[node]:
            heapq.heappush(candidate, connection)
print(answer)


