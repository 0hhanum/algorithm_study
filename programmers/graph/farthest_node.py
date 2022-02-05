'''
TRY1
def solution(n, edge):
    table = {}
    memo = {}

    def finder(current, counter):
        connected = []
        for e in edge[:]:
            if current in e:
                a, b = e
                n = a if b == current else b
                edge.remove(e)
                connected.append(n)
        if not connected:
            print(current, counter, "gotta")
            table.setdefault(current, [])
            table[current].append(counter)
            return
        else:
            for n in connected:
                print(current, n)
                finder(n, counter + 1)

    finder(1, 0)
    print(table)
    return table[max(table)]


# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]),
      4)
# print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
# print(solution(2, [[1, 2]]), 1)
# print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
# print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
# print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
# print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
# print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)
'''


## TRY 2
def solution(n, edges):
    counter = 0
    current = [1, ]
    tmp = set()
    memo = {1}
    while True:
        for node in current:
            for edge in edges[:]:
                if node in edge:
                    a, b = edge
                    next_node = a if b == node else b
                    edges.remove(edge)
                    if next_node in memo:
                        continue
                    else:
                        tmp.add(next_node)
                        memo.add(next_node)
        current = list(tmp)
        tmp = set()
        if not edges:
            break
    return len(current)


a = [1, 2, 3, 4]
a[:2] = [0, 0]
print(a)

# ANSWER

from collections import deque, defaultdict


def solution(n, edges):
    distance = [0 for i in range(n + 1)]
    connection = defaultdict(list)
    counter = 0
    for a, b in edges:
        connection[a].append(b)
        connection[b].append(a)

    queue = deque()
    queue.append(1)

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if not distance[current]:
                distance[current] = counter
                for i in connection[current]:
                    queue.append(i)
        counter += 1
    distance[1] = 0
    maximum = max(distance)
    return distance.count(maximum)
