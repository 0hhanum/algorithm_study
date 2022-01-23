def separateNumbers(s):
    # Write your code here
    length = len(s)
    start = s[0]
    target = start
    pointer = 1
    while len(start) <= length / 2:
        target = str(int(target) + 1)
        if s[pointer:].startswith(target):
            pointer += len(target)
            if pointer == length:
                print("YES", start)
                return
            elif pointer > length:
                print("NO")
                return
        else:
            try:
                start = s[:len(start) + 1]
                target = start
                pointer = len(start)
            except:
                print("NO")
                return
    print("NO")
    return


separateNumbers("45035996273704964503599627370497")
