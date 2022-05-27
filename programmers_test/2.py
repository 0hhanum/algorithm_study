from collections import defaultdict


def solution(rooms, target):
    answer = []
    room_table = {}
    name_table = {}
    count_table = defaultdict(list)

    for room in rooms:
        i = room.index("]")
        room_number = int(room[1: i])
        names = room[i + 1:].split(',')
        room_table[room_number] = set(names)  # 방번호 테이블
        for name in names:  # 사람 이름 테이블
            if name_table.get(name):
                name_table[name][0] += 1
                name_table[name][1].append(room_number)
            else:
                name_table[name] = [1, [room_number]]
    for name in name_table:
        count_table[name_table[name][0]].append(name)

    for count in sorted(count_table.keys()):
        people = sorted(count_table[count])
        tmp = defaultdict(list)
        for person in people:
            if person in room_table[target]:  # 해당 방에 자리 있으면 continue
                continue
            # 제일 가까운 방
            d = min(name_table[person][1], key=lambda x: abs(x - target))
            tmp[d].append(person)
        for k in sorted(tmp.keys(), key=lambda x: abs(x - target)):
            answer += tmp[k]
    return answer

