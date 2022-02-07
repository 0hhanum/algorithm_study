def solution(s):
    length = len(s)
    answer = length

    for i in range(1, length // 2 + 1):
        pointer = i
        tmp = ""
        counter = 1
        current = s[:i]
        while pointer <= length - i:
            target = s[pointer:pointer + i]
            if target == current:
                counter += 1
            elif counter != 1:
                # Add to tmp
                tmp += str(counter) + current
                counter = 1
            else:  # counter == 1 & target != current
                tmp += current
            current = target
            pointer += i
        tmp += target if counter == 1 else str(counter) + target
        tmp += s[pointer:]
        tmp_length = len(tmp)

        if answer > tmp_length:
            answer = tmp_length
    return answer
