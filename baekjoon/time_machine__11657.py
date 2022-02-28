import sys
from collections import defaultdict

city, bus = list(map(int, sys.stdin.readline().split()))
distance = [float('inf') for _ in range(city + 1)]
distance[1] = 0
graph = defaultdict(dict)

for _ in range(bus):
    a, b, t = list(map(int, sys.stdin.readline().split()))
    if graph[a].get(b):
        graph[a][b] = min(graph[a][b], t)
    else:
        graph[a][b] = t

for _ in range(city - 1):
    for current in graph:
        destinations = graph[current]
        for destination in destinations:
            if distance[destination] > distance[current] + graph[current][destination]:
                distance[destination] = distance[current] + graph[current][destination]
cycle = False
for current in graph:
    destinations = graph[current]
    for destination in destinations:
        if distance[destination] > distance[current] + graph[current][destination]:
            cycle = True
            break
    if cycle:
        break

if cycle:
    print(-1)
else:
    for d in distance[2:]:
        if d == float('inf'):
            print(-1)
        else:
            print(d)
