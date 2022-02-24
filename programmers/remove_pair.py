# "abccba"	1
# "abcccba"	0
# "abccccbaaa"	1
# "abccaabaa"	0
# "a"	0


def solution(s):
    # 스택
    answer = 0
    stack = [s[0], ]
    for i in s[1:]:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        answer = 1
    return answer
