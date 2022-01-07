def breakingRecords(scores):
    # Write your code here
    minimum = maximum = scores[0]
    result = [0, 0]
    for i in scores:
        if i < minimum:
            result[1] += 1
            minimum = i
        elif i > maximum:
            result[0] += 1
            maximum = i
    return result

# 최고, 최저기록 갱신
