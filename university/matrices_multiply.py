def multiply_matrices():
    global matrix1, matrix2

    matrix3 = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum_of_multiplies = 0
            for k in range(len(matrix1[0])):
                sum_of_multiplies += matrix1[i][k] * matrix2[k][j]
            row.append(sum_of_multiplies)
        matrix3.append(row)

    return matrix3


if __name__ == "__main__":
    a, b, c = [int(i) for i in input().split()]

    matrix1 = []
    matrix2 = []

    for i in range(a):
        row = [int(i) for i in input().split()]
        matrix1.append(row)

    for i in range(b):
        row = [int(i) for i in input().split()]
        matrix2.append(row)

    for i in multiply_matrices():
        print(*i)

