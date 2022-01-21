def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    answer = -1
    length = len(sticks)
    for i in range(length - 1, 1, -1):
        if sticks[i] < sticks[i - 1] + sticks[i - 2]:
            return (sticks[i - 2], sticks[i - 1], sticks[i])
    return (answer,)
