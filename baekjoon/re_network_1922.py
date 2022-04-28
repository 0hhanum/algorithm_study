import sys

# MST 문제 => 크루스칼 사용
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

edges = []
for _ in range(M):
    edges.append(list(map(int, sys.stdin.readline().split())))
edges = sorted(edges, key=lambda x: x[2])  # 간선 weight 오름차순 정렬

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
    i, j, w = edges.pop(0)
    i = find(i)
    j = find(j)
    if i != j:
        answer += w
        count += 1
        union(i, j)
print(answer)