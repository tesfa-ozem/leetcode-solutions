from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[List[int]]:
    row, col = len(matrix), len(matrix[0])

    right, left = 0, col - 1
    up, down = 0, row - 1
    spiral_matrix = [[0 for _ in range(col)] for _ in range(row)]

    value = 1

    while value <= row * col:
        # Going right
        for i in range(right, left + 1):
            spiral_matrix[up][i] = value
            value += 1
        up += 1

        # Moving down
        for i in range(up, down + 1):
            spiral_matrix[i][left] = value
            value += 1
        left -= 1

        # Moving left
        for i in range(left, right - 1, -1):
            spiral_matrix[down][i] = value
            value += 1
        down -= 1

        # Moving up
        for i in range(down, up - 1, -1):
            spiral_matrix[i][right] = value
            value += 1
        right += 1

    return spiral_matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))