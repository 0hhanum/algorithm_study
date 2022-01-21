from math import lcm, gcd


def solution(a, b):
    LCM = lcm(*a)
    GCD = current = gcd(*b)
    answer = 0
    while current <= GCD:
        if GCD % current == 0:
            answer += 1
        current += LCM
    return answer
