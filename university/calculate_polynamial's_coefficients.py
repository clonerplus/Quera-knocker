def give_indexes(i, limit1, limit2):
    return [(j, i-j) for j in range(i+1) if j < limit1 and i-j < limit2]


if __name__ == "__main__":
    m, n = [int(i) for i in input().split()]

    coeffs = [int(i) for i in input().split()]
    result = coeffs[:]
    if n == 1:
        print(' '.join(map(str, (i for i in result))))
        exit(0)

    for i in range(n-1):
        multiplies = []
        for j in range(len(result)+len(coeffs)-1):
            indxes = give_indexes(j, m+1, len(result))
            multiply = 0
            # print(indxes)
            for k in range(len(indxes)):
                multiply += coeffs[indxes[k][0]] * result[indxes[k][1]]
            multiplies.append(multiply)
        result = multiplies[:]

        # print(result, '***')
    print(*result)
