import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
heap = []
counter = 0
answer = 0

for _ in range(M):
    v1, v2, cost = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(heap, (cost, v1 - 1, v2 - 1))
table = [[0 for i in range(N)] for j in range(N)]


def dfs(start, target, memo, table):
    memo[start] = 1
    for i in range(N):
        if not table[start][i]:  # 연결 아니면 continue
            continue
        else:
            if i == target:
                memo[i] = 1
                return memo
            elif memo[i] != 1:
                dfs(i, target, memo, table)

while counter < N - 1:
    cost, v1, v2 = heapq.heappop(heap)
    memo = [0 for _ in range(N)]
    dfs(v1, v2, memo, table)
    if memo[v2] == 1:
        continue
    else:
        answer += cost
        counter += 1
        table[v1][v2] = 1
        table[v2][v1] = 1

print(answer)
