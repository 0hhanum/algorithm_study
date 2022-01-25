# TRT 1
def solution(number, k):
    answer = ''
    _number = number
    for index, c in enumerate(number[:-1]):
        if c < number[index + 1]:
            _number = _number.replace(c, "", 1)
            k -= 1
            if k == 0:
                break
    while k != 0:
        _number = _number.replace(min(number), "", 1)
        k -= 1
    return _number


# TRY2
def solution(number, k):
    _number = number
    _number = "".join(sorted(_number, reverse=True))
    counter = 0  # 확정된 자리의 수
    while k != 0:
        is_changed = number
        for i in _number[:]:
            d = number.find(i, counter)
            if d == -1:
                continue
            d -= counter  # distance
            if d <= k:
                k -= d
                _number.replace(i, "", 1)  # 찾으면 sort 리스트에서 삭제.
                number = number[0:counter] + number[d + counter:]
                counter += 1
                break
        if is_changed == number:
            break
    if k != 0:
        number = number[0:-k]
    return number


print(solution("54321", 4))


# print("4177252841".find("7", 3))
# print("abcde"[:-2])

# TRY3
def solution(number, k):
    _number = number
    _number = "".join(sorted(_number, reverse=True))
    counter = 0  # 확정된 자리의 수
    while k != 0:
        for i in _number[:]:
            d = number.find(i, counter)
            if d == -1:
                continue
            d -= counter  # distance
            if d <= k:
                k -= d
                _number.replace(i, "", 1)  # 찾으면 sort 리스트에서 삭제.
                number = number[0:counter] + number[d + counter:]
                counter += 1
                break
        if _number == number:  # 54321 이렇게 되어있어서 삭제할거 찾을 수 없을때
            break
    if k != 0:
        number = number[0:-k]
    return number
