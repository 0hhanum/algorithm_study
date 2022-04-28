import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[float('inf') for _ in range(N)] for __ in range(N)]

for _ in range(M):
    i, j, w = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    graph[i][j] = min(w, graph[i][j])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] = 0
                continue
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for row in graph:
    for num in row:
        print(num, end=" ")
    print()

