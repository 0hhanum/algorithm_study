def solution(survey, choices):
    answer = ''
    score = [0 for _ in range(4)]
    types = ["RT", "TR", "CF", "FC", "JM", "MJ", "AN", "NA"]

    for idx, s in enumerate(survey):
        choice = choices[idx]
        t = types.index(s)
        if t % 2 == 0:
            score[t // 2] += choice - 4
        else:
            score[t // 2] += -(choice - 4)

    print(score)
    for idx, s in enumerate(score):
        if s >= 0:
            answer += types[idx * 2][0]
        else:
            answer += types[idx * 2][1]
    return answer

