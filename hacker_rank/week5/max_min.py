def maxMin(k, arr):
    # Write your code here
    arr.sort()
    _arr = []
    minimum = float("inf")
    for i in range(len(arr) - k + 1):
        diff = arr[i + k - 1] - arr[i]
        if minimum > diff:
            minimum = diff
    return minimum
