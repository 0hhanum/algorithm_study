def heap_pop(heap):
    top_node = heap.pop(0)
    if len(heap) == 0:
        return top_node
    last_node = heap.pop()
    index = 0
    heap.insert(index, last_node)
    while True:
        a = index * 2 + 1
        b = a + 1
        try:
            a_node = heap[a]
            b_node = heap[b]
        except IndexError:
            return top_node
        if a_node > b_node:
            target = b
        else:
            target = a
        if heap[target] < last_node:
            heap[index] = heap[target]
            heap[target] = last_node
            index = target
        else:
            return top_node


def heap_add(heap, node):
    heap.append(node)
    index = len(heap) - 1
    if index == 0:
        return
    while True:
        if index % 2 == 0:
            target = int((index - 2) / 2)
        else:
            target = int((index - 1) / 2)
        if heap[target] > node:
            heap[index] = heap[target]
            heap[target] = node
            index = target
        else:
            return


def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        answer += 1
        a = heap_pop(scoville)
        b = heap_pop(scoville)
        heap_add(scoville, a + 2 * b)
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        scoville.sort()
    return answer


# 2트


def solution(scoville, K):
    answer = 0
    while scoville[0] < K:
        answer += 1
        a = min(scoville)
        scoville.remove(a)
        b = min(scoville)
        scoville.remove(b)
        scoville.append(a + 2 * b)
        i = min(scoville)
        scoville.remove(i)
        scoville.insert(0, i)
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer


# 3트

import heapq as h


def solution(scoville, K):
    h.heapify(scoville)
    i = 0
    while scoville[0] < K:
        i += 1
        a = h.heappop(scoville)
        b = h.heappop(scoville)
        h.heappush(scoville, a + 2 * b)
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return i


print(solution([1, 2, 3, 9, 10, 12], 7))
