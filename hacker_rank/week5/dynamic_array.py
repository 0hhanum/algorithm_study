def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    la = 0
    result = []

    for q, x, y in queries:
        idx = ((x ^ la) % n)
        if q == 1:
            arr[idx].append(y)
        else:
            la = arr[idx][y % len(arr[idx])]
            result.append(la)
    print(result)
    print(arr)
    return result
