import sys

n = int(sys.stdin.readline().strip())
stairs = [-1]
for i in range(n):
    stairs.append(int(sys.stdin.readline().strip()))

""" TRY1
def climb(start):
    answer = stairs[start]
    current = start
    while True:
        if current == n - 2 or current == n - 1:
            answer += stairs[n]
            break
        elif current == n:
            break
        s1 = stairs[current + 1]
        s2 = stairs[current + 2]
        if s1 > s2:
            answer += stairs[current + 1] + stairs[current + 3]
            current += 3
        else:  # 같은 경우도 포함
            answer += stairs[current + 2]
            current += 2
    return answer


if n > 3:
    print(max(climb(1), climb(2)))
elif n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1] + stairs[2])
elif n == 3:
    print(max(stairs[1] + stairs[3], stairs[2] + stairs[3]))
"""
if n > 2:
    memo = [[0, 0], [stairs[1], stairs[1]], [stairs[1] + stairs[2], stairs[2]],
            [stairs[2] + stairs[3], stairs[1] + stairs[3]]]
    for i in range(4, n + 1):
        root1 = memo[i - 1][1] + stairs[i]
        root2 = max(memo[i - 2]) + stairs[i]
        memo.append([root1, root2])
if n > 2:
    print(max(memo[-1]))
else:
    print(sum(stairs[1:]))

