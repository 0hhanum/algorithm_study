from collections import defaultdict
from math import ceil


def solution(logs):
    table = defaultdict(set)
    users = set()

    for log in logs:
        user, question = log.split()
        table[question].add(user)
        users.add(user)

    user_num = len(users)
    answer = sorted(list(filter(lambda x: len(table[x]) >= ceil(user_num / 2), table)))
    return answer

# 절반 이상 푼 웰노운문제 찾기
