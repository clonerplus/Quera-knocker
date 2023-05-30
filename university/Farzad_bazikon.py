def print_matrix(matrix):
    for i in matrix:
        print(i)
    print()
def multiply_matrices():
    global matrix1, matrix2, n
    matrix3 = []
    for i in range(n):
        row = []
        for j in range(n):
            multiply = 0
            for k in range(n):
                multiply += matrix1[i][k] * matrix2[k][j]

            row.append(multiply)
        matrix3.append(row)

    return matrix3

def matrix_determinant(mat, n):
    if n == 2:
        return mat[0][0]*mat[1][1] - mat[0][1] * mat[1][0]

    det = 0
    for i in range(n):
        # making matrix
        matrix = []
        for j in range(1, n):
            row = []
            for k in range(n):
                if k != i:
                    row.append(mat[j][k])
            matrix.append(row)

        # print_matrix(matrix)
        # multiply row element in sub matrix determinant
        det += (-1)**i * mat[0][i] * matrix_determinant(matrix, n-1)
    return det


if __name__ == "__main__":
    n = int(input())
    matrix1 = []
    matrix2 = []

    for i in range(n):
        matrix1.append([int(i) for i in input().split()])

    for i in range(n):
        matrix2.append([int(i) for i in input().split()])

    matrix = multiply_matrices()
    if matrix_determinant(matrix, n) % 2:
        print("Danial")
    else:
        print("Farzad")


"""
test case:
4
5 2 6 1
0 6 2 0
3 8 1 4
1 8 5 6
7 5 8 0
1 8 2 6
9 4 3 8
5 3 7 9
"""
