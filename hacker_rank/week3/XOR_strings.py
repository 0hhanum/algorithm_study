def strings_xor(s, t):
    result = ""
    for i, j in zip(s, t):
        if i == j:
            result += "0"
        else:
            result += "1"
    return result


s = "01010"
t = "10101"
print(strings_xor(s, t))
