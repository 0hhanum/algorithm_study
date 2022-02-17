def solution(record):
    answer = []
    result = []
    table = {}
    for r in record:
        try:
            keyword, uid, username = r.split(" ")
        except ValueError:
            keyword, uid = r.split(" ")
        if keyword == "Enter":
            table[uid] = username
            result.append((0, uid))
        elif keyword == "Leave":
            result.append((1, uid))
        else:
            table[uid] = username

    for keyword, uid in result:
        if keyword == 0:
            answer.append(f'{table[uid]}님이 들어왔습니다.')
        else:
            answer.append(f'{table[uid]}님이 나갔습니다.')

    return answer
