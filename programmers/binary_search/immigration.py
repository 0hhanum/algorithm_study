# 이진탐색 구현
def binary_search(array, x):
    start = 0
    end = len(array) - 1

    while start <= end:
        pointer = (end + start) // 2
        current = array[pointer]
        if current == x:
            return pointer
        elif current > x:
            start = start
            end = pointer - 1
        else:
            start = pointer + 1
            end = end
    return -1


def solution(n, times):
    times.sort()
    start = 0
    end = n * times[0]
    answer = 0

    def check(time):
        result = 0
        for i in times:
            result += time // i
        return result

    while start <= end:
        current = (start + end) // 2
        people = check(current)
        if people < n:
            start = current + 1
        else:
            end = current - 1
    return start


print(solution(6, [7, 10]))
