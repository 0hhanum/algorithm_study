# 간선이 100000 개. -> 크루스칼 보다는 프림으로 접근
import sys
import heapq
from collections import defaultdict

V, E = map(int, sys.stdin.readline().split())
answer = 0
table = defaultdict(list)
connected = set()
heap = []

for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().split())
    table[v1].append([w, v2])
    table[v2].append([w, v1])

heap.append([0, 1])

while heap:
    weight, current = heapq.heappop(heap)
    if current not in connected:
        answer += weight
        connected.add(current)
    for w, adjacent in table[current]:
        if adjacent not in connected:
            heapq.heappush(heap, [w, adjacent])

print(answer)
