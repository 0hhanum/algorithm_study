from itertools import combinations as cb


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
