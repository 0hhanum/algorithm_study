def diagonalDifference(arr):
    # Write your code here
    length = len(arr[0])
    a = b = 0
    index = 0
    for i in arr:
        a += i[index]
        b += i[length - index - 1]
        index += 1
    return abs(a - b)
