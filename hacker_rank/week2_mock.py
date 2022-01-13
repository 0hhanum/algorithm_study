def flippingMatrix(matrix):
    # Write your code here
    n = int(len(matrix) / 2)
    result = []
    for i in range(n):
        for j in range(n):
            result.append(max(matrix[i][j], matrix[i][2 * n - j - 1], matrix[2 * n - i - 1][j],
                              matrix[2 * n - i - 1][2 * n - j - 1]))
    return sum(result)
