if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]

    results = {str(i): 0 for i in range(1, n + 1)}
    aces = {str(i): {str(i): 0} for i in range(1, n + 1)}
    min_paths = {}
    min_paths_values = {"%s_%s" % (i, i): 0 for i in range(1, n + 1)}
    variable = []

    for i in range(m):
        line = input().split()
        aces[line[0]][line[1]] = int(line[2])
        variable.append((line[:2], int(line[2])))
        min_paths_values[line[0] + '_' + line[1]] = int(line[2])

    n_variable = []
    while variable:
        for i in variable:
            continuation = aces[i[0][-1]]
            for j in continuation:
                cost = continuation[j]
                key = i[0][0] + '_' + j
                try:

                    existing = min_paths_values[key]
                    if existing > i[1] + cost:
                        del aces[i[0][0]][j]
                        min_paths[key] = i[0] + [j]
                        min_paths_values[key] = i[1] + cost
                        n_variable.append(
                            (i[0] + [j], i[1] + cost))
                except KeyError:
                    min_paths[key] = i[0] + [j]
                    min_paths_values[key] = i[1] + cost
                    n_variable.append(
                        (i[0] + [j], i[1] + cost))

        variable = n_variable.copy()
        n_variable.clear()

    for i in min_paths.values():
        for j in range(1, len(i) - 1):
            results[i[j]] += 1

    print('\n'.join(map(str, [results[i] for i in results])))


"""
test case:
5 6
1 4 1
4 2 2
5 2 3
2 1 5
3 5 7
1 3 9

6 13
3 1 1
1 5 2
5 3 3
1 2 4
4 1 5
3 2 6
4 2 7
1 6 8
3 6 10
4 3 11
6 5 12
4 6 14
2 6 15

"""
