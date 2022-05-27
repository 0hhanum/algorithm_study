def solution(line):
    answer = []
    qwerty = 'QWERTYUIOP'
    nums = '1234567890'
    table = {}
    for i in range(10):
        table[qwerty[i]] = [i, 0]
        table[nums[i]] = [i, 1]

    left = [0, 0]
    right = [9, 0]

    for character in line:
        # 맨하탄 거리
        c = table[character]

        man_r = abs(right[0] - c[0]) + abs(right[1] - c[1])
        man_l = abs(left[0] - c[0]) + abs(left[1] - c[1])
        if man_r > man_l:
            left = c
            answer.append(0)
            continue
        elif man_r < man_l:
            right = c
            answer.append(1)
            continue

        # 수평 거리
        hor_r = abs(right[0] - c[0])
        hor_l = abs(left[0] - c[0])
        if hor_r > hor_l:
            left = c
            answer.append(0)
            continue
        elif hor_r < hor_l:
            right = c
            answer.append(1)
            continue

        # 다 같으면
        if c[0] < 5:
            answer.append(0)
            left = c
        else:
            answer.append(1)
            right = c

    return answer

