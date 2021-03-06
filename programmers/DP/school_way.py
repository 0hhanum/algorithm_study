def solution(m, n, puddles):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in puddles:
        x -= 1
        y -= 1
        grid[y][x] = -1
        if x == 0:
            for i in range(y, n):
                grid[i][x] = -1
        if y == 0:
            for i in range(x, m):
                grid[y][i] = -1
    for i in range(m):
        for j in range(n):
            try:
                if grid[j][i] == -1 and grid[j - 1][i + 1] == -1:
                    grid[j][i + 1] = -1
            except:
                pass

    def go_to_school(x, y, value, direction):
        if grid[y][x] == -1:
            return

        if x == 0 or y == 0:
            grid[y][x] = value
        elif direction == 1 and grid[y - 1][x] == -1:
            grid[y][x] = value
        elif direction == 0 and grid[y][x - 1] == -1:
            grid[y][x] = value
        elif direction == 1 and grid[y - 1][x] == 0:
            return
        elif direction == 0 and grid[y][x - 1] == 0:
            return
        else:
            value = grid[y - 1][x] + grid[y][x - 1]
            grid[y][x] = value

        if x + 1 < m:
            go_to_school(x + 1, y, value, 1)
        if y + 1 < n:
            go_to_school(x, y + 1, value, 0)

    go_to_school(0, 0, 1, 1)

    return grid[-1][-1] % 1000000007 if grid[-1][-1] != -1 else 0
