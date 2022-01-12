def solution(priorities, location):
    answer = 0
    queue = list(enumerate(priorities))
    target = queue[location]
    while target in queue:
        index, item = queue[0]
        prior = max(queue, key=lambda x: x[1])[1]
        del queue[0]
        if item == prior:
            answer += 1
        else:
            queue.append((index, item))
    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
