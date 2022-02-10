from collections import defaultdict


def solution(n, costs):
    answer = 0
    table = defaultdict(list)
    memo = [[0 for i in range(n)] for _ in range(n)]
    for a, b, cost in costs:
        table[cost].append((a, b))
    counter = 0

    def dfs(a, tmp):
        tmp[a] = 1
        for i in range(n):
            connect = memo[a][i]
            if connect == 0:
                continue
            if connect == 1 and tmp[i] == 0:
                dfs(i, tmp)

    while counter < n - 1:
        minimum = min(table.keys())
        a, b = table[minimum].pop()
        if not table[minimum]:
            table.pop(minimum)

        tmp = [0 for _ in range(n)]
        dfs(a, tmp)
        # 그룹에 있으면 continue
        if tmp[b] == 1:
            continue
        else:
            memo[b][a] = 1
            memo[a][b] = 1
        # 없으면 이어준다.
        counter += 1
        answer += minimum
    return answer
