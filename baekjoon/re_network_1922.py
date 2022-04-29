import heapq
import sys

# MST 문제 => 크루스칼 사용
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

edges = []
for _ in range(M):
    a, b, w = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(edges, [w, a, b])

# UNION FIND
root = [i for i in range(N + 1)]


def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return find(root[x])


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    root[x] = y


count = 0
answer = 0
while count < N - 1:
    w, a, b = heapq.heappop(edges)
    a = find(a)
    b = find(b)
    if a != b:
        answer += w
        count += 1
        union(a, b)
print(answer)
