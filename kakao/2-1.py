def solution(queue1, queue2):
    answer = -1
    length = len(queue1)
    whole_queue = queue1 + queue2

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2 != 0:
        return -1
    target = (sum1 + sum2) // 2

    for i in range(length):
        if i == length - 1:
            for j in range(length):
                if i + j < length:
                    s = sum(whole_queue[j: j + i])
                else:
                    s = sum(whole_queue[j:]) + sum(whole_queue[:(j + i) % length])
                if s == target:
                    break
        else:
            for j in range(length * 2):
                if i + j < length:
                    s = sum(whole_queue[j: j + i])
                else:
                    s = sum(whole_queue[j:]) + sum(whole_queue[:(j + i) % length])
                if s == target:
                    break

    return answer
