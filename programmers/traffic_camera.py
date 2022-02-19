def solution(routes):
    answer = 1
    routes.sort()

    current = routes.pop(0)

    while routes:
        target = routes.pop(0)
        if target[1] < current[1]:  # 포함되는 경우
            current = target
        elif target[0] > current[1]:  # 넘어가는 경우
            answer += 1
            current = target
        elif target[0] <= current[1]:  # 겹치는 경우
            current[0] = target[0]

    return answer
