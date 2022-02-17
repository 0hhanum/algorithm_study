def solution(lottos, win_nums):
    answer = []
    zero = 0
    hit = 0

    for i in lottos:
        if i in win_nums:
            hit += 1
        elif i == 0:
            zero += 1

    answer = [7 - (hit + zero) if 7 - (hit + zero) <= 5 else 6, 7 - hit if 7 - hit <= 5 else 6]

    return answer
