a = "12345622"
total_len, split_len = len(a), 3
a = [a[i:i + split_len] for i in range(0, total_len, split_len)]
print(a)


# 파이썬 문자열 길이로 자르기 테크닉


def solution(answers):
    result = [0, 0, 0]
    answer1 = "".join(["12345" for _ in range(8)])
    answer2 = "".join(["21232425" for _ in range(5)])
    answer3 = "".join(["3311224455" for _ in range(4)])

    total_len, split_len = len(answers), 40
    splited_answers = [answers[i: i + split_len] for i in range(0, total_len, split_len)]

    for answer in splited_answers:
        i = 0
        for a in answer:
            a = str(a)
            if a == answer1[i]:
                result[0] += 1
            if a == answer2[i]:
                result[1] += 1
            if a == answer3[i]:
                result[2] += 1
            i += 1
    best_score = max(result)
    answer = []
    for i in range(3):
        if result[i] == best_score:
            answer.append(i + 1)
    return answer
