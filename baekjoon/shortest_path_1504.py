import heapq
import sys

N, E = map(int, sys.stdin.readline().strip().split())
graph = {i: {} for i in range(1, N + 1)}

for _ in range(E):
    v1, v2, d = map(int, sys.stdin.readline().strip().split())
    graph[v1][v2] = min(graph[v1].get(v2, float('inf')), d)
    graph[v2][v1] = min(graph[v2].get(v1, float('inf')), d)

t1, t2 = map(int, sys.stdin.readline().strip().split())

start_distance = [float('inf') for _ in range(N + 1)]

heap = [[1, 0]]
start_distance[1] = 0

while heap:
    current, d = heapq.heappop(heap)
    if start_distance[current] < d:
        continue
    for target, target_d in graph[current].items():
        total_d = d + target_d
        if start_distance[target] > total_d:
            start_distance[target] = total_d
            heapq.heappush(heap, [target, total_d])

middle_distance1 = [float('inf') for _ in range(N + 1)]
middle_distance2 = [float('inf') for _ in range(N + 1)]
heap1 = []
heap2 = []
middle_distance1[t1] = 0
middle_distance2[t2] = 0
if start_distance[t1] != float('inf'):
    heap1.append([t1, 0])
if start_distance[t2] != float('inf'):
    heap2.append([t2, 0])

while heap1:
    current, d = heapq.heappop(heap1)
    if middle_distance1[current] < d:
        continue
    for target, target_d in graph[current].items():
        total_d = d + target_d
        if middle_distance1[target] > total_d:
            middle_distance1[target] = total_d
            heapq.heappush(heap1, [target, total_d])
while heap2:
    current, d = heapq.heappop(heap2)
    if middle_distance2[current] < d:
        continue
    for target, target_d in graph[current].items():
        total_d = d + target_d
        if middle_distance2[target] > total_d:
            middle_distance2[target] = total_d
            heapq.heappush(heap2, [target, total_d])

answer = min(start_distance[t1] + middle_distance1[t2] + middle_distance2[N], start_distance[t2] + middle_distance2[t1] + middle_distance1[N])
if answer != float('inf'):
    print(answer)
else:
    print(-1)
