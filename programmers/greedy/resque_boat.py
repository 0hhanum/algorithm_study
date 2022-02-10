from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()  # 정렬
    people = deque(people)
    num = len(people)
    counter = 0
    while num >= 2:
        heavy = people[-1]
        light = people[0]
        if heavy + light <= limit:
            people.popleft()
            people.pop()
            num -= 2
        else:
            people.pop()
            num -= 1
        counter += 1

    return counter if num == 0 else counter + 1
