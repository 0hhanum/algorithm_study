def sorting(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            a = array[j]
            b = array[j + 1]
            if a < b and a + b < b + a:
                tmp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = tmp
    return array


# 버블정렬 변형을 이용한 풀이 -> 시간초과로 실패

def solution(numbers):
    answer = ''
    stack = []
    string_nums = [str(i) for i in numbers]
    string_nums.sort(reverse=True)
    print(string_nums)
    for s in string_nums:
        if stack:
            tmp = []
            while stack[-1].startswith(s):
                tmp.append(stack.pop())
                if not stack:
                    break
            if tmp:
                stack += tmp
        stack.append(s)
    for s in stack:
        answer += s
    return answer


a = ["12", "23", "2241", "120", "3", "330", "30"]
print(solution(a))
