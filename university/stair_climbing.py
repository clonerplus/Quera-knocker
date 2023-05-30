def stair_combinations(n):
    if n in str_combs.keys():
        return str_combs[n]

    if n >= 5:
        return stair_combinations(n-5) + stair_combinations(n-2) + stair_combinations(n-1)

    return stair_combinations(n-2) + stair_combinations(n-1)


n = int(input())

str_combs = {0: 1, 1: 1, 2: 2}

print(stair_combinations(n))
