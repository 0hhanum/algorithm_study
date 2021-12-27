"""
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false 를
 그렇지 않으면 true 를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book 의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.
"""


# 1트
# 길이 기준으로 딕셔너리 만들어서 본인보다 긴 것 찾기

def solution_1(phone_book):
    table = {}
    phone_book.sort(key=len)

    for i in range(1, 21):
        table[i] = []

    answer = True
    for number in phone_book:
        table[len(number)].append(number)

    for number in phone_book:
        length = len(number)
        for i in range(length + 1, 21):
            for num in table[i]:
                if num.startswith(number):
                    answer = False
                    break

    return answer


# 2
# 정렬해놓고 무식하게 기
def solution(phone_book):
    phone_book.sort(key=len)
    answer = True
    length = len(phone_book)
    for i in range(length):
        for j in range(i + 1, length):
            if phone_book[j].startswith(phone_book[i]):
                answer = False
                return answer
    return answer


solution(["119", "97674223", "1195524421", "121"])
a = ["119", "97674223", "1195524421", "121"]
a.sort()
print(a)
for i, j in zip(a, a[1:]):
    print(i, j)


# 3
def solution(phone_book):
    for number in phone_book:
        temp = ''
        for digit in number:
            temp += digit
            if temp in phone_book and temp != number:
                return False
    return True


# 4
def solution(phone_book):
    table = {}
    for number in phone_book:
        table[number] = 1
    for number in phone_book:
        temp = ''
        for digit in number:
            temp += digit
            if temp in table and temp != number:
                return False
    return True
