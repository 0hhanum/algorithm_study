def migratoryBirds(arr):
    # Write your code here
    table = {}
    for i in arr:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1

    maximum = max(table, key=table.get)
    result = []
    for key, value in table.items():
        if value == table[maximum]:
            result.append(key)
    result.sort()
    return result[0]
