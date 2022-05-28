from math import ceil


def solution(n, times):
    memo = [float('inf') for _ in range(n + 1)]
    memo[1] = 0
    t_len = ceil(n / 2)

    for i in range(1, n):
        for j in range(1, min(i, t_len) + 1):
            try:
                memo[i + j] = min(memo[i + j], memo[i] + times[j - 1])
            except:
                break
    return memo[n]

# 무한 길이 줄 나눠 최소로 N 개로 만들기