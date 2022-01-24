import heapq as hp


def solution(operations):
    max_heap = []
    min_heap = []

    for i in operations:
        if i.startswith("I"):
            num = int(i[2:])
            hp.heappush(max_heap, (-num, num))
            hp.heappush(min_heap, num)
        else:
            command = i[2]
            if min_heap:
                if command == "1":
                    num = hp.heappop(max_heap)[1]
                    min_heap.remove(num)
                    hp.heapify(min_heap)
                else:
                    num = hp.heappop(min_heap)
                    max_heap.remove((-num, num))
                    hp.heapify(max_heap)
    if min_heap:
        return [hp.heappop(max_heap)[1], hp.heappop(min_heap)]
    else:
        return [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
