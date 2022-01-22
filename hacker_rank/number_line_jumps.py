def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 == x2:
        return "YES"
    elif x1 > x2 and v1 >= v2:
        return "NO"
    elif x1 < x2 and v1 <= v2:
        return "NO"
    else:
        speed = abs(v2 - v1)
        a = min(x1, x2)
        b = max(x1, x2)
        while b > a:
            a += speed
            if a == b:
                return "YES"
        return "NO"
