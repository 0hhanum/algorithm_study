import sys


def get_index(arr, x, start, end):
    mid = (start + end) // 2
    if arr[mid] <= x <= arr[mid + 1]:
        return mid
    elif arr[mid] > x:
        return get_index(arr, x, start, mid - 1)
    elif arr[mid + 1] < x:
        return get_index(arr, x, mid + 1, end)


def find(arr, x, start, end):
    mid = (start + end) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return find(arr, x, start, mid - 1)
    elif arr[mid] < x:
        return find(arr, x, mid + 1, end)


n, k = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readlines()))
current = [array[0]]
answer = 0
length = 1
if k == 1:
    answer += current[0]
for i, x in enumerate(array[1:]):
    if current[0] >= x:
        current.insert(0, x)
    elif current[-1] <= x:
        current.append(x)
    else:
        current.insert(get_index(current, x, 0, length) + 1, x)
    length += 1
    if length > k:
        current.pop(find(current, array[i + 1 - k], 0, length))
        length -= 1
    if length == k:
        answer += current[(k - 1) // 2]
print(answer)
