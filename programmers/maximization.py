from itertools import permutations

ex = ['+', '-', '*']
permutation = list(permutations(ex))


def solution(expression):
    answer = 0
    for p in permutation:
        first = expression.split(p[0])
        second = []
        for f in first:
            second.append(f.split(p[1]))
        for s in second:
            for i, _s in enumerate(s):
                s[i] = str(eval(_s))
        for i, s in enumerate(second):
            first[i] = str(eval(p[1].join(s)))
        result = abs(eval(p[0].join(first)))
        answer = max(result, answer)
    return answer
