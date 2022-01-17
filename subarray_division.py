def birthday(s, d, m):
    # Write your code here
    length = len(s)
    result = 0
    for i in range(0, length - m + 1):
        if sum(s[i:i + m]) == d:
            result += 1
    return result
