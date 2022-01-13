def flippingBits(n):
    result = ""
    while n > 1:
        result += str(n % 2)
        n = n // 2
    result += str(n)
    result = result[::-1]
    tmp = ""
    for s in result:
        tmp += "1" if s == "0" else "0"
    result = tmp
    length = 32 - len(result)
    result = "".join(["1" for _ in range(length)]) + result

    return int(result, 2)
