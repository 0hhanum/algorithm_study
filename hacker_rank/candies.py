from collections import deque


def candies(n, arr):
    # Write your code here
    dq = deque()
    direction = -1
    result = [0 for _ in range(n)]
    for idx, i in enumerate(arr):
        if idx == n - 1:
            if direction == -1:
                dq.append(idx)
                continue
        else:
            if direction == -1:
                direction = 1 if i < arr[idx + 1] else 0
                dq.append(idx)
                continue
            tmp = 1 if arr[idx + 1] > i else 0
        if direction == tmp:
            if direction:
                dq.append(idx)
            else:
                dq.appendleft(idx)
        else:
            if direction:
                dq.append(idx)
            else:
                dq.appendleft(idx)
            i = 1
            for _ in range(len(dq)):
                index = dq.popleft()
                result[index] = i
                i += 1
            direction = -1
    i = 1
    for _ in range(len(dq)):
        index = dq.popleft()
        result[index] = i
        i += 1
    print(sum(result))
    return sum(result)


def candies(n, arr):
    result = [1 for _ in range(n)]
    for idx, i in enumerate(arr[:-1]):
        if i < arr[idx + 1]:
            result[idx + 1] = result[idx] + 1
    for i in range(n - 1, 0, -1):
        if arr[i - 1] > arr[i] and result[i - 1] <= result[i]:
            result[i - 1] = result[i] + 1
    return sum(result)


A = [0, 0, 0, ]
for i, j in enumerate(A):
    print(i, j)
