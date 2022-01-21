def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    for x, y in zip(A, B):
        if x + y < k:
            return "NO"
    return "YES"
