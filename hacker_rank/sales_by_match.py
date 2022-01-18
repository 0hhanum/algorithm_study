def sockMerchant(n, ar):
    # Write your code here
    table = {}
    result = 0
    for sock in ar:
        if sock in table:
            del table[sock]
            result += 1
        else:
            table[sock] = 0
    return result
