def solution(atmos):
    answer = 0
    state = [[80, 150], [35, 75]]

    mask = 0

    for m, c in atmos:
        if m > 150 and c > 75:  # 폐기
            if mask:
                mask = 0
            else:
                answer += 1
            continue
        elif m > 80 or c > 35:  # 마스크 써야함
            if mask:
                mask += 1
            else:  # 안 썼으면
                mask = 1
                answer += 1
        else:  # 좋아도 mask counter ++
            if mask:
                mask += 1
        if mask == 3:
            mask = 0
    return answer
