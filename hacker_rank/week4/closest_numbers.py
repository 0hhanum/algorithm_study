def closestNumbers(arr):
    # Write your code here
    arr.sort()
    table = {}
    for i, a in enumerate(arr[:-1]):
        value = abs(a - arr[i + 1])
        if value not in table:
            table[value] = [a, arr[i + 1]]
        else:
            table[value] += [a, arr[i + 1]]
    min_value = min(table)
    return table[min_value]
