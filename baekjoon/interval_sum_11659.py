import math
import random
import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
nums = []
N, M = random.randint(1, 100000), random.randint(1, 100000)
for _ in range(N):
    nums.append(random.randint(1, 1000))
nums.insert(0, 0)  # 노드 번호와 인덱스 일치시키기
intervals = []
tree = [0 for _ in range(2 ** (math.ceil(math.log2(100000)) + 1) + 1)]  # 트리 구성


def init(start, end, index):
    if start == end:
        tree[index] = nums[start]
        return tree[index]
    else:
        mid = (start + end) // 2
        tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
        return tree[index]


def query(start, end, l, r, index):
    if (l > end) or (r < start):
        return 0
    if start >= l and end <= r:
        return tree[index]
    mid = (start + end) // 2
    return query(start, mid, l, r, index * 2) + query(mid + 1, end, l, r, index * 2 + 1)


init(1, N, 1)

for _ in range(M):
    l, r = map(int, sys.stdin.readline().strip().split())
    print(query(1, N, l, r, 1))
