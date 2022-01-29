def maxDifference(px):
    # Write your code here
    result = 0
    minimum = px[0]
    print(px)
    for current in px:
        if current <= minimum:
            minimum = current
            continue
        else:
            diffrence = current - minimum
            if diffrence > result:
                result = diffrence
    return result if result != 0 else -1

# 주식 최대 가격차이 묻는 문제
