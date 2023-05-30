def give_tile_combinations(length):
    if length in tile_combinations.keys():
        return tile_combinations[length]

    if length % 2 == 0:
        # tile_combinations[length] =
        return give_tile_combinations(length // 2) ** 2 + give_tile_combinations((length // 2) - 1) ** 2

    # else
    return give_tile_combinations((length - 1) // 2) ** 2 + \
        2 * give_tile_combinations((length // 2) - 1) * give_tile_combinations(length // 2)


n = int(input())
tile_combinations = {0: 1, 1: 1, 2: 2, 3: 3}

print(give_tile_combinations(n))
