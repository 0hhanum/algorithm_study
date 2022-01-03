"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres 와 노래별 재생 횟수를 나타내는 정수 배열 plays 가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로
 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres 와 plays 의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

"""

'''
steps 
1. 가장 많이 재생된 장르 찾기 
How? table 에 장르별로 횟수 기록? index 기록?
table is like => [total, (play, index), (play, index), ... ]
그냥 상위 두개만 기록 ?
2. 그 순서대로 상위 두 개씩 가져와 result 에 삽입.
'''


def solution(genres, plays):
    table = {}
    for (index, genre), play in zip(enumerate(genres), plays):
        if genre not in table:
            table[genre] = [play, (play, index)]
        else:
            table[genre][0] += play
            length = len(table[genre][1:])
            if length == 1:
                if play > table[genre][1][0]:
                    table[genre].insert(1, (play, index))
                else:
                    table[genre].append((play, index))
            else:
                first, second = table[genre][1][0], table[genre][2][0]
                if play > first and play > second:
                    table[genre].insert(1, (play, index))
                    del table[genre][3]
                elif play > second:
                    table[genre].insert(2, (play, index))
                    del table[genre][3]

    # total 값 순으로 정렬
    new_table = sorted(table.items(), key=lambda x: x[1][0], reverse=True)
    answer = []

    for item in new_table:
        try:
            first, second = item[1][1][1], item[1][2][1]
            answer.append(first)
            answer.append(second)
        except:
            first = item[1][1][1]
            answer.append(first)
    return answer


a = ["classic", "pop", "classic", "classic", "pop"]
b = [500, 600, 150, 800, 2500]
print(solution(a, b))
