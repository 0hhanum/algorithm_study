def pickingNumbers(a):
    # Write your code here
    a.sort()
    current = a[0]
    length = max_answer = 1
    toggle = True
    for i in a[1:]:
        diffrence = abs(i - current)
        if diffrence == 0:
            length += 1
        elif diffrence == 1 and toggle:
            length += 1
            toggle = False
        else:
            if length > max_answer:
                max_answer = length
            length = 1
            toggle = True
        current = i
    if length > max_answer:
        max_answer = length
    return max_answer
