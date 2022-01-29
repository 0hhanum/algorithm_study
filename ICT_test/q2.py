def getMaxUnits(boxes, unitsPerBox, truckSize):
    # Write your code here
    result = 0
    unitsPerBox = sorted(enumerate(unitsPerBox), key=lambda x: x[1], reverse=True)
    # 박스당 개수 최대순으로 정렬
    for index, UPB in unitsPerBox:
        available = boxes[index]
        if available >= truckSize:  # 트럭 용량이 가능한 상자 용량보다 적을 경우, 가능한 만큼만 싣는다.
            result += (truckSize * UPB)
            break
        result += (available * UPB)
    return result
