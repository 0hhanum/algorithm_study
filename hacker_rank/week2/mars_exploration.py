def marsExploration(s):
    # Write your code here
    times = int(len(s) / 3)
    expected = ""
    result = 0
    for _ in range(times):
        expected += "SOS"
    for i in range(times * 3):
        if expected[i] != s[i]:
            result += 1
    return result
