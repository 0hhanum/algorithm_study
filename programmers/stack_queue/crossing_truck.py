# 1트
def solution(bridge_length, weight, truck_weights):
    tick = 1
    queue = [0 for i in range(bridge_length)]
    queue[-1] = truck_weights.pop(0)
    while sum(queue) != 0:
        queue.pop(0)
        queue.append(0)
        if truck_weights and sum(queue) + truck_weights[0] <= weight:
            queue[-1] = truck_weights.pop(0)
        tick += 1
    return tick


print(solution(2, 10, [7, 4, 5, 6]))


# 2 트
def solution2(bridge_length, weight, truck_weights):
    tick = 1
    queue = [0 for i in range(bridge_length)]
    queue[-1] = truck_weights.pop(0)
    while truck_weights:
        queue.pop(0)
        queue.append(0)
        if sum(queue) + truck_weights[0] <= weight:
            queue[-1] = truck_weights.pop(0)
        tick += 1
    return tick + bridge_length


# 3
def solution(bridge_length, weight, truck_weights):
    tick = 1
    queue = [0 for i in range(bridge_length)]
    queue[-1] = truck_weights.pop(0)
    total = sum(queue)
    while truck_weights:
        out = queue.pop(0)
        if out != 0:
            total -= out
        queue.append(0)
        if total + truck_weights[0] <= weight:
            queue[-1] = truck_weights.pop(0)
            total += queue[-1]
        tick += 1
    return tick + bridge_length
