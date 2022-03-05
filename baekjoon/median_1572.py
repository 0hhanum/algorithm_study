import sys
import heapq
n, k = list(map(int, sys.stdin.readline().strip().split(" ")))
temperature = []
answer = 0
if k == 1:
    for _ in range(n):
        answer += int(sys.stdin.readline().strip())
    print(answer)
else:
    for i in range(k):
        temperature.append(int(sys.stdin.readline().strip()))

    _temperature = temperature[:]
    temperature.sort()
    mid_index = (k + 1) // 2 - 1
    median = temperature[mid_index]
    max_heap = [[-i, i] for i in temperature[:mid_index + 1]]
    max_heap.reverse()
    min_heap = temperature[mid_index + 1:]
    answer = median
    l_length = mid_index + 1
    r_length = k - l_length
    for i in range(n - k):
        new_temp = int(sys.stdin.readline().strip())
        _temperature.append(new_temp)
        old_temp = _temperature[i]

        if old_temp <= median:
            max_heap.remove([-old_temp, old_temp])
            heapq.heapify(max_heap)
            l_length -= 1
            if old_temp == median:
                if r_length == l_length:
                    median = max_heap[0][1]
                else:
                    median = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, [-median, median])
                    r_length -= 1
                    l_length += 1
            elif l_length < r_length:
                median = heapq.heappop(min_heap)
                heapq.heappush(max_heap, [-median, median])
                r_length -= 1
                l_length += 1
        else:
            min_heap.remove(old_temp)
            heapq.heapify(min_heap)
            r_length -= 1
            if l_length - r_length >= 2:
                tmp = heapq.heappop(max_heap)[1]
                heapq.heappush(min_heap, tmp)
                l_length -= 1
                r_length += 1
                median = max_heap[0][1]

        if new_temp <= median:
            heapq.heappush(max_heap, [-new_temp, new_temp])
            l_length += 1
            if l_length > r_length + 1:
                tmp = heapq.heappop(max_heap)[1]
                heapq.heappush(min_heap, tmp)
                l_length -= 1
                r_length += 1
        else:
            heapq.heappush(min_heap, new_temp)
            r_length += 1
            if r_length > l_length:
                tmp = heapq.heappop(min_heap)
                heapq.heappush(max_heap, [-tmp, tmp])
                l_length += 1
                r_length -= 1
        median = max_heap[0][1]
        answer += median
    print(answer)
#
# import sys
# while True:
#     try:
#         import heapq
#         import random
#         n, k = random.randint(1, 250000), random.randint(1, 5000)
#         if n < k:
#             n, k = k, n
#         answer = 0
#         if k == 1:
#             for i in range(n):
#                 answer += random.randint(0, 65536)
#             print(answer)
#         else:
#             temperature = []
#             for i in range(k):
#                 temperature.append(random.randint(0, 65536))
#             _temperature = temperature[:]
#             temperature.sort()
#             mid_index = (k + 1) // 2 - 1
#             median = temperature[mid_index]
#             max_heap = [[-i, i] for i in temperature[:mid_index + 1]]
#             max_heap.reverse()
#             min_heap = temperature[mid_index + 1:]
#             answer = median
#             l_length = mid_index + 1
#             r_length = k - l_length
#             for i in range(n - k):
#                 new_temp = random.randint(0, 30)
#                 _temperature.append(new_temp)
#                 old_temp = _temperature[i]
#
#                 print(_temperature)
#                 print(max_heap, min_heap)
#                 print("median",median)
#                 print("new_temp",new_temp)
#                 print("old_temp",old_temp)
#                 print()
#
#                 if old_temp <= median:
#                     max_heap.remove([-old_temp, old_temp])
#                     heapq.heapify(max_heap)
#                     l_length -= 1
#                     if old_temp == median:
#                         if r_length == l_length:
#                             median = max_heap[0][1]
#                         else:
#                             median = heapq.heappop(min_heap)
#                             heapq.heappush(max_heap, [-median, median])
#                             r_length -= 1
#                             l_length += 1
#                     elif l_length < r_length:
#                         median = heapq.heappop(min_heap)
#                         heapq.heappush(max_heap, [-median, median])
#                         r_length -= 1
#                         l_length += 1
#                 else:
#                     min_heap.remove(old_temp)
#                     heapq.heapify(min_heap)
#                     r_length -= 1
#                     if l_length - r_length >= 2:
#                         tmp = heapq.heappop(max_heap)[1]
#                         heapq.heappush(min_heap, tmp)
#                         l_length -= 1
#                         r_length += 1
#                         median = max_heap[0][1]
#
#                 if new_temp <= median:
#                     heapq.heappush(max_heap, [-new_temp, new_temp])
#                     l_length += 1
#                     if l_length > r_length + 1:
#                         tmp = heapq.heappop(max_heap)[1]
#                         heapq.heappush(min_heap, tmp)
#                         l_length -= 1
#                         r_length += 1
#                 else:
#                     heapq.heappush(min_heap, new_temp)
#                     r_length += 1
#                     if r_length > l_length:
#                         tmp = heapq.heappop(min_heap)
#                         heapq.heappush(max_heap, [-tmp, tmp])
#                         l_length += 1
#                         r_length -= 1
#                 median = max_heap[0][1]
#                 answer += median
#             print(answer)
#     except IndexError:
#         break
#     except ValueError:
#         print(123123)
#         break
#     print("----------------")