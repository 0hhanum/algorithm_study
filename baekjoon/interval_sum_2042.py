import math
import sys

N, M, K = map(int, sys.stdin.readline().strip().split())
nums = []
tree = [0 for _ in range(2 ** (math.ceil(math.log2(N)) + 1) + 1)]  # 트리 구성
nums.insert(0, 0)


def init(start, end, index):
    if start == end:
        tree[index] = nums[start]
        return tree[index]
    else:
        mid = (start + end) // 2
        tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
        return tree[index]


def get_sum(start, end, l, r, index):
    if end < l or start > r:
        return 0
    if l <= start and end <= r:
        return tree[index]
    mid = (start + end) // 2
    return get_sum(start, mid, l, r, index * 2) + get_sum(mid + 1, end, l, r, index * 2 + 1)


def modify(start, end, index, target, difference):
    if target < start or end < target:  # 범위 벗어나면 종료
        return
    if start == end:
        tree[index] = nums[target]
        return
    if start <= target <= end:
        mid = (start + end) // 2
        tree[index] += difference
        modify(start, mid, index * 2, target, difference)
        modify(mid + 1, end, index * 2 + 1, target, difference)


for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))
init(1, N, 1)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == 1:
        d = c - nums[b]
        nums[b] = c
        modify(1, N, 1, b, d)
    else:
        print(get_sum(1, N, b, c, 1))
        # pass
