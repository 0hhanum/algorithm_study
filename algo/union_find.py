def solution(n, computers):
    answer = 0
    rank = [i for i in range(n)]
    root = [i for i in range(n)]

    def find(x):
        if x == root[x]:
            return x
        root[x] = find(root[x])
        return find(root[x])

    def union(x, y):
        x = find(x)
        y = find(y)
        if rank[x] < rank[y]:
            root[x] = y
        else:
            root[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    for x, y, isConnected in computers:
        if isConnected:
            union(x, y)
    for i in range(n):
        find(i)
    connected = set()
    for i in root:
        if i not in connected:
            connected.add(i)
            answer += 1
    return answer
