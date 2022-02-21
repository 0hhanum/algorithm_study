def solution(numbers, hand):
    answer = ''
    l = [0, 1]
    r = [0, 1]
    l_num = [7, 4, 1]
    r_num = [9, 6, 3]
    m_num = [0, 8, 5, 2]
    for number in numbers:
        if number in l_num:
            answer += "L"
            l = [l_num.index(number) + 1, 1]
        elif number in r_num:
            answer += "R"
            r = [r_num.index(number) + 1, 1]
        else:
            target = m_num.index(number)
            l_distance = abs(target - l[0]) + l[1]
            r_distance = abs(target - r[0]) + r[1]

            if l_distance > r_distance:
                answer += "R"
                r = [m_num.index(number), 0]
            elif l_distance < r_distance:
                answer += "L"
                l = [m_num.index(number), 0]
            else:
                if hand == "right":
                    answer += "R"
                    r = [m_num.index(number), 0]
                else:
                    answer += "L"
                    l = [m_num.index(number), 0]
    return answer
