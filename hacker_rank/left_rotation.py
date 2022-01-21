def rotateLeft(d, arr):
    # Write your code here
    length = len(arr)
    d = d % length
    arr = arr[d:] + arr[0: d]
    return arr
