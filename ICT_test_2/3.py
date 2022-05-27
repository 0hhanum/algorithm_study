#!/bin/python


# Complete the function below.

# 건너뛰는게 더 좋은 선택일 수 있음
def findLIS(arr, N):
    length = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                length[i] = max(length[i], length[j] + 1)
    return max(length)


_s_cnt = int(input())
_s_i = 0
_s = []
while _s_i < _s_cnt:
    _s_item = int(input());
    _s.append(_s_item)
    _s_i += 1
res = findLIS(_s, _s_cnt);
print(res)
