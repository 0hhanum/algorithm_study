def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    result = ""
    for i in s:
        if "A" <= i <= "Z":
            i = ord(i) + k
            if i > 90:
                i = 65 + i - 91
            i = chr(i)
        elif "a" <= i <= "z":
            i = ord(i) + k
            if i > 122:
                i = 97 + i - 123
            i = chr(i)
        print(i)
        result += i
    return result
