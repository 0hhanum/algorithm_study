import heapq
import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

for _ in range(N):
    n, d, c = map(int, sys.stdin.readline().strip().split())
    times = [float('inf') for _ in range(n + 1)]
    times[c] = 0
    heap = [[0, c]]
    table = defaultdict(list)
    maximum = 0
    counter = 0
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().strip().split())
        table[b].append([s, a])

    while heap:
        current_time, current = heapq.heappop(heap)
        if current_time > times[current]:
            continue
        if table[current]:
            for target_time, target in table[current]:
                total_time = current_time + target_time
                if total_time < times[target]:
                    times[target] = total_time
                    heapq.heappush(heap, [total_time, target])
    for time in times:
        if time == float('inf'):
            continue
        if time > maximum:
            maximum = time
        counter += 1
    print(counter, maximum)
