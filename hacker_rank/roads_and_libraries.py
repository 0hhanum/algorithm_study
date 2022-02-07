counter = 0


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    global counter
    table = {i: set() for i in range(n)}
    memo = [0 for _ in range(n)]
    group = 0

    for x, y in cities:
        x -= 1
        y -= 1
        table[x].add(y)
        table[y].add(x)

    def dfs(node):
        global counter
        if memo[node]:
            return
        else:
            memo[node] = 1
            counter += 1
            for i in table[node]:
                dfs(i)

    result = []
    for i in range(n):
        if not memo[i]:
            counter = 0
            dfs(i)
            group += 1
            result.append(counter)
    answer = 0
    if c_lib > c_road:
        for i in result:
            answer += c_lib
            answer += (i - 1) * c_road

    else:
        answer = n * c_lib
    return answer
