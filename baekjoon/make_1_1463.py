import sys

num = int(sys.stdin.readline().strip())
#
# def solution(n):
#     print(n)
#     if n in table:
#         print("gotta")
#         return table[n]
#     else:
#         if n % 3 == 0:
#             value = min(1 + solution(n // 3), solution(n - 1) + 1)
#         elif n % 2 == 0:
#             value = min(1 + solution(n // 2), solution(n - 1) + 1)
#         else:
#             value = min(1 + solution(n - 1), solution(n - 2) + 2)
#         table[n] = value
#         return value
#
# print(solution(num))
# print(table)

table = [0, 0, 1, 1]  # 0 1 2 3
for i in range(4, 10**6 + 1):
    if i % 6 == 0:
        table.append(min(table[i // 3] + 1, table[i // 2] + 1))
    elif i % 3 == 0:
        table.append(min(table[i // 3] + 1, table[i - 1] + 1))
    elif i % 2 == 0:
        table.append(min(table[i // 2] + 1, table[i - 1] + 1))
    else:
        table.append(min(table[i - 2] + 2, table[i - 1] + 1))
print(table[num])