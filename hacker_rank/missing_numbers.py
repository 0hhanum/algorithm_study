def missingNumbers(arr, brr):
    # Write your code here
    table = defaultdict(int)
    for i in brr:
        table[i] += 1
    for i in arr:
        table[i] -= 1
        if table[i] == 0:
            del table[i]
    result = list(table.keys())
    result.sort()
    return result
