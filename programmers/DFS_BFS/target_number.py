from itertools import combinations as cb
from itertools import product


def solution(numbers, target):
    answer = 0
    for i, _ in enumerate(numbers):
        temp = list(cb(numbers, i))
        for tuple in temp:
            number_copy = numbers.copy()
            for item in tuple:
                number_copy.remove(item)
                number_copy.append(-item)
            if sum(number_copy) == target:
                answer += 1

    return answer


a = [2, 4, 6]
l = [(x, -x) for x in a]
print(l)
print(list(product(l)))
print(list(product(*l)))
print(list(product((1, 2, 3), (4, 5), (7,))))
