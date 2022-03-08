import sys


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
    else:
        x_rank = rank[x]
        y_rank = rank[y]
        if x_rank > y_rank:
            root[y] = x
        else:
            root[x] = y
            rank[y] += 1


def func(x):
    return int(x) - 1


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
root = [i for i in range(N)]
rank = [0 for _ in range(N)]

for current in range(N):
    connection = map(int, sys.stdin.readline().strip().split())
    for neighbor, path in enumerate(connection):
        if path == 1:
            if find(current) == find(neighbor):
                continue
            else:
                union(current, neighbor)
        else:
            continue

plan = list(map(func, sys.stdin.readline().strip().split()))
reference = find(plan[0])
answer = True
for city in plan[1:]:
    if find(city) != reference:
        answer = False
        break
if answer:
    print("YES")
else:
    print("NO")
