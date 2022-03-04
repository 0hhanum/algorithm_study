import sys
sys.setrecursionlimit(10**7)
num = int(sys.stdin.readline().strip())

table = {2: 1, 3: 1}


def solution(n):
    print(n)
    if n in table:
        print("gotta")
        return table[n]
    else:
        if n % 3 == 0:
            value = min(1 + solution(n // 3), solution(n - 1) + 1)
        elif n % 2 == 0:
            value = min(1 + solution(n // 2), solution(n - 1) + 1)
        else:
            value = min(1 + solution(n - 1), solution(n - 2) + 2)
        table[n] = value
        return value

print(solution(num))
print(table)
