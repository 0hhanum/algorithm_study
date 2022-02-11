def solution(n):
    answer = ''
    q = 1
    while q:
        q = n // 3
        r = n % 3
        if r == 0:
            r = 3
            q -= 1
        n = q
        answer += str(r)
    answer = list(answer[::-1])

    for i in range(len(answer)):
        if answer[i] == "3":
            answer[i] = "4"
    answer = "".join(answer)
    return answer
