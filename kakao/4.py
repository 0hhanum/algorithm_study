from collections import defaultdict

def solution(n, paths, gates, summits):
    answer = [-1, float('inf')]
    graph = defaultdict(list)

    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    def dfs(current, intensity, visited):
        if visited[current] == 1:
            return
        elif visited[current] == -1:  # 입구
            return
        elif visited[current] == -2:  # 도착
            if answer[1] > intensity:
                answer[0] = current
                answer[1] = intensity
            elif answer[1] == intensity:
                answer[0] = min(current, answer[0])
        else:
            visited[current] = 1  # 방문
            for target, cost in graph[current]:
                if cost > answer[1]:
                    continue
                if cost > intensity:
                    dfs(target, cost, visited)
                else:
                    dfs(target, intensity, visited)

    visited = [0 for _ in range(n + 1)]
    for g in gates:
        visited[g] = -1
    for summit in summits:
        visited[summit] = -2
    for gate in gates:
        for path, w in graph[gate]:
            dfs(path, w, visited[:])
    return answer


