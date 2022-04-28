def solution(new_id):
    answer = new_id.lower()
    tmp = answer[:]
    dot_toggle = False

    removed = 0
    for i in range(len(answer)):
        if answer[i] in "~!@#$%^&*()=+[{]}:?,<>/":
            tmp = tmp.replace(tmp[i - removed], "")
            removed += 1
        # if answer[i] == "." and dot_toggle:
        #     tmp = tmp.replace(tmp[i - removed], "")
        #     removed += 1
        #     dot_toggle = False
        # elif answer[i] == "." and not dot_toggle:
        #     dot_toggle = True
    answer = tmp
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))