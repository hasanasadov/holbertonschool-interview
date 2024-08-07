def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    """Rotate a 2D matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
        matrix (list[list]): a 2D matrix to rotate
    """'''
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # current number
            # Current number
            tmp = matrix[i][j]
            # change top for left
            # Change top for left
            matrix[i][j] = matrix[x][i]
            # change left for bottom
            # Change left for bottom
            matrix[x][i] = matrix[y][x]
            # change bottom for right
            # Change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            # Change right for top
            matrix[j][y] = tmp


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_2d_matrix(matrix)
    print(matrix)  # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
