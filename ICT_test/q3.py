def minimizeCost(numPeople, x, y):
    # Write your code here
    result = 0

    start = (min(x), min(y))
    end = (max(x), max(y))
    row = abs(start[0] - end[0]) + 1
    column = abs(start[1] - end[1]) + 1
    matrix = [[0 for i in range(row)] for i in range(column)]
    minValue = 0

    for idx, (_x, _y) in enumerate(zip(x, y)):
        _x -= start[0]
        _y -= start[1]
        # 시작점 기준으로 생각
        for j in range(column):
            for i in range(row):
                matrix[j][i] += (abs(i - _x) + abs(j - _y)) * numPeople[idx]
    for i in range(row):
        for j in range(column):
            value = matrix[j][i]
            minValue = value if (value < minValue) or minValue == 0 else minValue
            # 행렬 최소값 찾기
    return minValue


x = [1, 2, 3]
y = [4, 5, 6]
for index, (_x, _y) in enumerate(zip(x, y)):
    print(index, _x, _y)

print(minimizeCost([1, 2], [1, 3], [1, 3]))
print(minimizeCost([1, 1, 1], [5, 2, 3], [3, 4, 7]))
