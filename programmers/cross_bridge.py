def solution(stones, k):
    answer = 0
    length = len(stones)
    minimum = min(stones)
    while True:
        counter = 0
        tmp = float('inf')
        # print(stones)
        # print(minimum)
        answer += minimum
        for i in range(length):
            if stones[i] == 0:
                counter += 1
                if counter == k:
                    return answer
                continue
            stones[i] -= minimum
            if stones[i] == 0:
                counter += 1
                if counter == k:
                    return answer
                else:
                    continue
            elif counter:
                counter = 0
            if stones[i] < tmp and stones[i] != 0:
                tmp = stones[i]
        minimum = tmp


# 무조건 answer 뺴면 안됨.. min = 3 일때 2만 빼면 될수도있음.

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


def solution(stones, k):
    answer = 0
    for i in range(len(stones) - k + 1):
        tmp = stones[i: i + k]
        minimum = min(tmp)
        maximum = max(tmp)
        if maximum - minimum <= k:
            answer = maximum
    return answer

# 무조건 answer 뺴면 안됨.. min = 3 일때 2만 빼면 될수도있음.
