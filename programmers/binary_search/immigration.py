# 이진탐색 구현
def binary_search(array, x):
    start = 0
    end = len(array) - 1

    while start <= end:
        pointer = (end + start) // 2
        current = array[pointer]
        if current == x:
            return pointer
        elif current > x:
            start = start
            end = pointer - 1
        else:
            start = pointer + 1
            end = end
    return -1


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in range(14):
    print(i, " : ", binary_search(a, i))
