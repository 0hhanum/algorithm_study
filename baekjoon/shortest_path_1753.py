import heapq
import sys
from collections import defaultdict

V, E = list(map(int, sys.stdin.readline().split()))
start = int(sys.stdin.readline())
table = defaultdict(list)
weights = [float('inf') for _ in range(V + 1)]
weights[start] = 0
heap = [[0, start]]

for _ in range(E):  # 인접 리스트 만들기
    u, v, w = list(map(int, sys.stdin.readline().split()))
    table[u].append((w, v))
while heap:
    current_weight, current = heapq.heappop(heap)
    if current_weight < weights[current]:  # 더 짧은 경로가 있을 경우 pass
        continue
    if table[current]:
        for target_weight, target in table[current]:
            total_weight = current_weight + target_weight
            if total_weight < weights[target]:

                weights[target] = total_weight
                heapq.heappush(heap, [total_weight, target])


# 답
for weight in weights[1:]:
    if weight == float('inf'):
        print("INF")
    else:
        print(weight)
