def solution(prices):
    answer = [999 for i in prices]
    stack = []
    for i in range(len(prices)):
        item = prices[i]
        for j in stack:  # 한바퀴 돌때마다 스택에 담겨있던 시간 +1
            j[1] += 1
        if not stack:  # stack 비어있다면
            stack.append([item, 0])
            continue
        elif stack[-1][0] > item:  # 스택 top > item 라면 -> 빼내야함
            tmp = []
            while stack and stack[-1][0] > item:
                _, frequency = stack.pop()
                tmp.append(frequency)
            for j in range(0, i):
                if answer[i - j - 1] == 999:
                    answer[i - j - 1] = tmp.pop(0)
                if not tmp:
                    break
        stack.append([item, 0])

    def converter(x):
        if x == 999:
            return stack.pop(0)[1]
        else:
            return x

    answer = list(map(converter, answer))
    return answer


# print(solution([1, 2, 3, 2, 3]))
# print(solution([3, 1, 3, 4, 1, 2]))
print(solution([1, 2, 3, 2, 1, 5, 1, 1, 1, 1, 1, 3, 3, 3, 3, 31, 3, 1, 3, 1, 3, 1, 31]))
