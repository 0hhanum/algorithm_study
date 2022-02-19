from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        tmp = defaultdict(int)
        for order in orders:
            for combination in combinations(order, c):
                combination = sorted(list(combination))
                combination = "".join(combination)
                tmp[combination] += 1
        if tmp:
            maximum = tmp[max(tmp, key=lambda x: tmp[x])]
            if maximum > 1:
                answer.extend(list(filter(lambda x: tmp[x] == maximum, tmp)))
    answer.sort()
    return answer
