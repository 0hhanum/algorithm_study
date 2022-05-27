def solution(rc, operations):
    def shift(matrix):
        matrix = [matrix[-1]] + matrix[:-1]
        return matrix

    def rotate(matrix):
        tmp = matrix[0][-1]
        matrix[0] = matrix[0][:-1]
        for row in matrix[1:-1]:
            tmp_ = row[-1]
            row[-1] = tmp
            tmp = tmp_
        matrix[-1].append(tmp)
        tmp = matrix[-1].pop(0)
        for row in matrix[-2:0:-1]:
            tmp_ = row[0]
            row[0] = tmp
            tmp = tmp_
        matrix[0].insert(0, tmp)

    for op in operations:
        if op == "ShiftRow":
            rc = shift(rc)
        else:
            rotate(rc)
    return rc

