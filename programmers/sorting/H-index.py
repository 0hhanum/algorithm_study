# 1트

def solution(citations):
    table = {}
    for i in citations:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1
        tmp = list(filter(lambda x: x < i, table))
        for j in tmp:
            table[j] += 1
    print(table)
    owner = list(filter(lambda x: x <= table[x], table))
    return max(owner)


# 2
table = {}
a = [1, 2, 3, 4]
for i in a:
    table[i] = 0


# 3
def solution(citations):
    table = {}
    citations.sort()
    for i in citations:
        table.setdefault(i, 0)
    for i in citations:
        tmp = list(filter(lambda x: x <= i, table))
        for j in tmp:
            table[j] += 1
    print(table)
    owner = list(filter(lambda x: x <= table[x], table))
    print(owner)
    return max(owner)


a = [5, 5, 5, 5]
a = [22, 42]
a = [20, 19, 18, 1]
a = [4, 0, 6, 1, 5]
a = [10, 2, 3, 4, 12, 34, 23, 12, 412, 120, 124, 12, 23, 34, 4, 6]


# print(solution(a))
# print(solution(a))


# 3 트
def solution(citations):
    citations.sort()
    total = len(citations)
    for index, num in enumerate(citations):
        if (total - index) <= num:
            return total - index
    return 0


print(solution([0, 0, 0]))
