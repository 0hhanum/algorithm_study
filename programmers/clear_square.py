def solution(w, h):
    answer = 0
    gradient = w / h

    for i in range(1, h):
        height = gradient * i
        answer += int(height)
    from math import gcd

    def solution(w, h):
        answer = 0
        gradient = w / h
        GCD = gcd(w, h)
        gw = int(w / GCD)
        gh = int(h / GCD)
        for i in range(1, int(h / GCD)):
            height = gradient * i
            answer += int(height)
        answer *= GCD
        answer += (gw * gh) * int(((1 + GCD - 1) * (GCD - 1) / 2))
        return answer * 2

    return answer * 2


# FAIL

from math import gcd


def solution(w, h):
    GCD = gcd(w, h)
    gw = int(w / GCD)
    gh = int(h / GCD)

    cut = gw + gh - 1
    return w * h - cut * GCD
