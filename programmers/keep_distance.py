def solution(places):
    answer = []
    for place in places:
        tmp = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    memo = [[0 for i in range(5)] for _ in range(5)]
                    result = []
                    finder(place, (i, j), i, j, memo, 0, result)
                    if result:
                        tmp = True
                        answer.append(1)
                        break
            if tmp:
                break
        if not tmp:
            answer.append(0)
    return answer


def finder(graph, start, x, y, memo, count, result):
    if (x, y) == start:  # 사방으로 보내기
        memo[x][y] = 1
        count += 1
        finder(graph, start, x - 1, y - 1, memo, count, result)
        finder(graph, start, x - 1, y + 1, memo, count, result)
        finder(graph, start, x + 1, y - 1, memo, count, result)
        finder(graph, start, x + 1, y + 1, memo, count, result)

    if result or count > 2:
        # 결과가 나왔거나, 2칸 이상 이동했거나, 이미 방문한 점이면 종료
        return
    try:
        current = graph[x][y]
        visited = memo[x][y]
    except IndexError:
        return
    if visited:
        return
    memo[x][y] = 1
    count += 1

    if current == "P" and count <= 2:  # hit
        result.append(1)
        return
    elif current == "X":
        return
    else:  # 비어있는 경우 -> 사방으로 보낸다
        finder(graph, start, x - 1, y - 1, memo, count, result)
        finder(graph, start, x - 1, y + 1, memo, count, result)
        finder(graph, start, x + 1, y - 1, memo, count, result)
        finder(graph, start, x + 1, y + 1, memo, count, result)
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))