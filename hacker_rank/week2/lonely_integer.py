def lonelyinteger(a):
    # Write your code here
    table = {}
    for i in a:
        if i not in table:
            table[i] = 1
        else:
            del table[i]
    return list(table.keys())[0]
