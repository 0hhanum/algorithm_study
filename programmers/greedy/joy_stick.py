# TRY 1
def finder(character):
    answer = 0
    _ord = ord(character)
    if _ord <= 78:
        return _ord - 65
    else:
        return 91 - _ord


def solution(name):
    answer = 0
    length = len(name)
    if name == "A":
        return 0
    _name = name
    for i, c in enumerate(name):
        answer += finder(c)
        _name = _name[1:]
        if _name == "A" * len(_name):
            _name = ""
            break
        if name[i + 1] == "A":
            break
        if len(_name) != 0:
            answer += 1
    if _name:
        answer += 1 + i
        _name = _name[::-1]
        __name = _name
        for i, c in enumerate(_name):
            answer += finder(c)
            __name = __name[1:]
            if __name == "A" * len(__name):
                __name = ""
                break
            if len(__name) != 0:
                answer += 1
    return answer


#
#
# print(solution("AAAABABAAAA"))
# print(solution("ABABAABA"))


def solution(name):
    move = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    answer = idx = 0
    length = len(name)
    while True:
        answer += move[idx]
        move[idx] = 0
        if sum(move) == 0:
            break
        left = right = 1
        next_move = 0
        while True:
            next_left = move[idx - left]
            next_right = move[idx + right]
            if next_right != 0:
                next_move = right
                break
            elif next_left != 0:
                next_move = -left
                break
            next_left += 1
            next_right += 1
        idx += next_move
        answer += abs(next_move)
    return answer


# 3

def solution(name):
    move = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    answer = idx = 0
    length = len(name)
    while True:
        answer += move[idx]
        move[idx] = 0
        if sum(move) == 0:
            break
        right = 1
        left = -1
        while True:
            next_left = move[idx + left]
            if next_left != 0:
                break
            left -= 1
        while True:
            next_right = move[idx + right]
            if next_right != 0:
                break
            right += 1
        if right <= abs(left):
            next_move = right
        else:
            next_move = left
        idx = idx + next_move
        answer += abs(next_move)
    return answer


# print(solution("ABAAAAAAAAABB"))

# ANSWER
from collections import deque
from itertools import product


def solution(name):
    results = []

    for rs in product((-1, 1), repeat=len(name) - 1):
        name_deque = deque(name)
        default = deque('A' * len(name))

        for c, r in enumerate([0] + list(rs)):
            default.rotate(r)
            name_deque.rotate(r)
            default[0] = name_deque[0]

            if name_deque == default:
                results.append(c)
                break

    return min(set(results)) + sum([min(ord(l) - ord('A'), ord('Z') - ord(l) + 1) for l in name])
