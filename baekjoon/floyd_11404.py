import sys

C = int(sys.stdin.readline())
B = int(sys.stdin.readline())

graph = [[float('inf') if i != j else 0 for i in range(C + 1)] for j in range(C + 1)]

for _ in range(B):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    if graph[u][v] > w:
        graph[u][v] = w

for k in range(1, C + 1):
    for i in range(1, C + 1):
        for j in range(1, C + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, C + 1):
    for j in range(1, C + 1):
        value = graph[i][j]
        if value != float('inf'):
            print(value, end=" ")
        else:
            print(0, end=" ")
    print()