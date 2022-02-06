def solution(n, results):
    answer = 0
    table = {i: [0 for i in range(n)] for i in range(n)}
    for win, lose in results:
        win -= 1
        lose -= 1
        table[win][lose] = 1
        table[lose][win] = -1

    for i in range(n):
        for j in range(len(table[i])):
            if table[i][j] == 1:
                loser = table[j]
                for k in range(n):
                    if loser[k] == 1:
                        table[i][k] = 1
                        table[k][i] = -1
            elif table[i][j] == -1:
                winner = table[j]
                for k in range(n):
                    if winner[k] == -1:
                        table[i][k] = -1
                        table[k][i] = 1

    for li in table.values():
        if li.count(0) == 1:
            answer += 1
    return answer
