def solution(n, lost, reserve):
    answer1 = 0
    answer2 = 0
    tmp = lost.copy()
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            tmp.remove(i)
    lost = tmp
    lost.sort()
    for num in lost:
        # 둘다면 왼쪽
        a = (num - 1) in reserve
        b = (num + 1) in reserve
        if a and b:
            reserve.remove(num - 1)
        elif a:
            reserve.remove(num - 1)
        elif b:
            reserve.remove(num + 1)
        else:
            answer1 += 1
    for num in lost:
        # 둘다면 오른쪽
        a = (num - 1) in reserve
        b = (num + 1) in reserve
        if a and b:
            reserve.remove(num + 1)
        elif a:
            reserve.remove(num - 1)
        elif b:
            reserve.remove(num + 1)
        else:
            answer2 += 1
    answer1 = n - answer1
    answer2 = n - answer2
    return answer1
