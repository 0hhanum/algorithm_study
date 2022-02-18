def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    current = 540  # 현재 시각 분으로 표기

    while n:
        n -= 1
        capacity = m

        while capacity:
            crew = timetable[0]
            hour, minute = crew.split(":")
            time = int(hour) * 60 + int(minute)
            if time <= current:
                timetable.pop(0)
                capacity -= 1
                if capacity == 0 and n == 0:
                    answer = time - 1
                    break
                if not timetable:
                    if capacity != 0:
                        answer = current
                        break
                    else:
                        answer = time + 1
                        break
            else:
                if n == 0:
                    answer = current
                    break
                else:
                    break
        current += t
    h = answer // 60
    m = answer % 60
    if h < 10:
        h = "0" + str(h)
    else:
        h = str(h)
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)
    answer = h + ":" + m
    return answer
