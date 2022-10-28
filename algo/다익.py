import heapq


def solution(N, road, K):
    answer = 0
    graph = [{i: 0} for i in range(N)]
    distance = [float('inf') for i in range(N)]
    distance[0] = 0
    heap = [[0, 0]]
    for a, b, c in road:
        if graph[a - 1].get(b-1, float('inf')) > c:
            graph[a - 1][b - 1] = c
            graph[b - 1][a - 1] = c
    while heap:
        d, current = heapq.heappop(heap)
        if d < distance[current]:
            distance[current] = d

        for target, target_d in graph[current].items():

            if distance[target] > d + target_d:
                distance[target] = d + target_d
                heapq.heappush(heap, [d + target_d, target])

    for d in distance:
        if d <= K:
            answer += 1
    return answer