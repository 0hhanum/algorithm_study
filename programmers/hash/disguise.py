"""
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
스파이가 가진 의상들이 담긴 2차원 배열 clothes 가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes 의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes 의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.

"""
from itertools import combinations


# 1트
def solution(clothes):
    table = {}
    for name, kind in clothes:
        try:
            table[kind].append(name)
        except KeyError:
            table[kind] = [name]
    kinds = list(table.keys())
    num_of_kinds = len(kinds)
    print(table)
    answer = 0

    # 5개면. 5개, 4개, 3개, 2개, 1개 순으로 해야함
    for i in range(1, num_of_kinds + 1):
        # print(list(combinations(kinds, i)))
        for selected_kind in list(combinations(kinds, i)):
            answer += finder(table, selected_kind)

    return answer


def finder(table, selected):
    answer = 1
    for kind in selected:
        answer *= len(table[kind])
    return answer


# 2트
def solution(clothes):
    table = {}
    for name, kind in clothes:
        try:
            table[kind].append(name)
        except KeyError:
            table[kind] = [name]

    for kind in table:
        table[kind] = len(table[kind])
    simplified_list = list(table.values())
    answer = 0
    for i in range(1, len(simplified_list) + 1):
        for selected in list(combinations(simplified_list, i)):
            answer += multiply(selected)

    return answer


def multiply(li):
    result = 1
    for i in li:
        result *= i
    return result


# 3트

def solution(clothes):
    table = {}
    for name, kind in clothes:
        try:
            table[kind].append(name)
        except KeyError:
            table[kind] = [name]

    for kind in table:
        table[kind] = len(table[kind]) + 1
    simplified_list = list(table.values())
    return multiply(simplified_list) - 1


a = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["pur", "glasses"]]
print(solution(a))
a = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(a))
