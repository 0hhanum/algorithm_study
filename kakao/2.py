from collections import deque


def solution(queue1, queue2):
    answer = -1
    length = len(queue1)
    limit = (length - 1) * (length * 2) + length
    count = 0
    find = False

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1 + sum2) % 2 != 0:
        return -1
    target = (sum1 + sum2) // 2
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while count < limit + 1 and count < 1000000:
        if sum1 > sum2:
            item = queue1.popleft()
            queue2.append(item)
            sum1 -= item
            sum2 += item
            count += 1
        elif sum1 < sum2:
            item = queue2.popleft()
            queue1.append(item)
            sum2 -= item
            sum1 += item
            count += 1
        else:
            find = True
            break
    if find:
        answer = count
    return answer
