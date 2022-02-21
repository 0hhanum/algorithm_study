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
def solution(stones, k):
    answer = float('inf')  # 가장 작은 최대값 찾기

    for i in range(len(stones) - k + 1):
        tmp = stones[i: i + k]
        maximum = max(tmp)
        if maximum <= answer:
            answer = maximum
    return answer


def solution(stones, k):
    # 이진탐색 문제
    start = 0
    end = max(stones)
    answer = 0
    while start <= end:
        mid = (end + start) // 2
        answer = mid
        _stones = list(map(lambda x: x - mid, stones))
        counter = 0
        for stone in _stones:
            if stone <= 0:
                counter += 1
            else:
                counter = 0
            if counter >= k:
                break
        if counter >= k:
            end = mid - 1
        else:
            start = mid + 1
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


def solution(stones, k):
    # 이진탐색 문제
    start = 0
    end = max(stones)
    while start <= end:
        mid = (end + start) // 2
        counter = 0
        for stone in stones:
            stone = stone - mid
            if stone <= 0:
                counter += 1
            else:
                counter = 0
            if counter >= k:
                break
        if counter >= k:
            end = mid - 1
        else:
            start = mid + 1
    return start
