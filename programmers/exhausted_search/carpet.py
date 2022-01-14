def solution(brown, yellow):
    start = int((brown / 2 + 2.0) / 2)
    end = int(brown / 2 - 1.0)
    for x in range(start, end + 1):
        y = brown / 2 + 2 - x
        if (x - 2) * (y - 2) == yellow:
            answer = [x, y]

    return answer
