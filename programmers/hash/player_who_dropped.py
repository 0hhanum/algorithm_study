"""
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant 와 완주한 선수들의 이름이 담긴 배열 completion 이 주어질 때,
 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
"""


# 1트
def solution(participant, completion):
    table = {}
    for player in participant:
        try:
            table[player] += 1
        except KeyError:
            table[player] = 1
    for player in completion:
        table[player] -= 1
        if table[player] == 0:
            del table[player]

    answer = list(table.keys())[0]
    return answer


p = ["marina", "josipa", "nikola", "vinko", "filipa"]
c = ["josipa", "filipa", "marina", "nikola"]
print(solution(p, c))
