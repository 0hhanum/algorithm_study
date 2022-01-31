# TRY1

def solution(triangle):
    answer = set()
    bottom = len(triangle)

    def find_max(floor, index, value):
        if floor == bottom:
            answer.add(value)
            return
        value += triangle[floor][index]
        floor += 1

        find_max(floor, index, value)
        find_max(floor, index + 1, value)

    find_max(0, 0, 0)

    return max(answer)


# TRY 2
def solution(triangle):
    answer = set()
    bottom = len(triangle)

    def find_max(floor, index, value):
        num = triangle[floor][index]
        if num == -1:
            return
        triangle[floor][index] = -1
        value += num
        floor += 1
        if floor == bottom:
            answer.add(value)
            return
        if triangle[floor][index] > triangle[floor][index + 1]:
            find_max(floor, index, value)
            find_max(floor, index + 1, value)
        else:
            find_max(floor, index + 1, value)
            find_max(floor, index, value)

    find_max(0, 0, 0)

    return max(answer)


# TRY 3
def solution(triangle):
    answer = set()
    top = len(triangle) - 1

    def finder(layer, index, value):
        value += triangle[top - layer][index]
        layer_length = len(triangle[top - layer]) - 1
        layer += 1

        if layer == top:
            answer.add(value + triangle[0][0])
            return
        if index == 0:
            finder(layer, 0, value)
        elif index == layer_length:
            finder(layer, index - 1, value)
        else:
            v1 = triangle[top - layer][index - 1]
            v2 = triangle[top - layer][index]
            if v1 > v2:
                finder(layer, index - 1, value)
            elif v1 < v2:
                finder(layer, index, value)
            else:
                finder(layer, index - 1, value)
                finder(layer, index, value)

    for i in range(top + 1):
        finder(0, i, 0)
    print(answer)
    return max(answer)


# TRY 4
def solution(triangle):
    answer = [0 for _ in triangle[-1]]
    top = len(triangle)
    for idx, num in enumerate(triangle[-1]):
        i = idx
        answer[i] += num
        for j in range(1, top):  # 제일 밑층부터 꼭대기까지
            nums = triangle[-1 - j]
            if i == 0:
                answer[idx] += nums[0]
            elif i - 1 == top - 1 - j:
                answer[idx] += nums[-1]
                i -= 1
            else:
                v1 = nums[i - 1]
                v2 = nums[i]
                if v1 > v2:
                    answer[idx] += nums[i - 1]
                    i -= 1
                else:
                    answer[idx] += nums[i]
    return max(answer)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


def solution(triangle):
    _triangle = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    answer = []
    length = len(triangle)
    for i in range(length):
        for j in range(i + 1):
            if j == 0:
                _triangle[i][j] += (_triangle[i - 1][j] + triangle[i][j])
            elif i == j:
                _triangle[i][j] += (_triangle[i - 1][j - 1] + triangle[i][j])
            else:
                v1 = _triangle[i - 1][j - 1]
                v2 = _triangle[i - 1][j]
                if v1 > v2:
                    _triangle[i][j] += (_triangle[i - 1][j - 1] + triangle[i][j])
                else:
                    _triangle[i][j] += (_triangle[i - 1][j] + triangle[i][j])

    return max(_triangle[-1])
