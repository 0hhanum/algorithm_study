# 간선이 100000 개. -> 크루스칼 보다는 프림으로 접근
import sys
import heapq
from collections import defaultdict

V, E = map(int, sys.stdin.readline().split())
answer = 0
table = defaultdict(list)
connected = [0 for i in range(V + 1)]
heap = [[0, 1]]

for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().split())
    table[v1].append([w, v2])
    table[v2].append([w, v1])

counter = 0

while heap:
    if counter == V:
        break
    weight, current = heapq.heappop(heap)
    if not connected[current]:
        answer += weight
        connected[current] = 1
        counter += 1
        for w, adjacent in table[current]:
            if not connected[adjacent]:
                heapq.heappush(heap, [w, adjacent])

print(answer)
