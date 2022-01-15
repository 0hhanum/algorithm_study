table = {}
answer = 0


def solution(n, computers):
    global table
    global answer

    def seek(index):
        global table
        global answer
        network = computers[index]
        if index not in table:
            answer += 1
            table[index] = 0
        for i, edge in enumerate(network):
            if i == index:
                continue
            if edge == 1:
                if i not in table:
                    table[i] = 0
                    seek(i)

    for index, network in enumerate(computers):
        if index in table:
            continue
        seek(index)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
