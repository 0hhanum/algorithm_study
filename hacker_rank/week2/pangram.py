def pangrams(s):
    # Write your code here
    table = {}
    for i in range(65, 91):
        table[i] = 0

    for i in s:
        code = ord(i.upper())
        if code in table:
            del table[code]
    if not table:
        return "pangram"
    return "not pangram"
