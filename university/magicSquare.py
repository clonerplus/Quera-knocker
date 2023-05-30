def print2darray(arr):
    for i in arr:
        print(*i)


def is_square_empty():
    global square
    for i in square:
        if 0 in i:
            return True
    return False


def fill_the_square():
    global square, m, n

    i, j, k = 0, (n+1)//2-1, m
    square[i][j] = m
    k += 1
    ii, jj = i, j
    while is_square_empty():
        # print2darray(square)
        # print()
        i -= 1
        j += 1
        if i == -1:
            i = n-1
        if j == n:
            j = 0
        if square[i][j]:
            i, j = ii+1, jj
        square[i][j] = k
        k += 1
        ii, jj = i, j
        # print(ii, jj)


if __name__ == "__main__":

    n, m = [int(i) for i in input().split()]

    square = [[0 for i in range(n)] for j in range(n)]

    fill_the_square()

    print2darray(square)