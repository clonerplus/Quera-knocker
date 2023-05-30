n = int(input())

funcs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

move = 0
num = 1
i, j = (0, 0)
m = 0
start = True
while start:
    for k in range(2):
        if n-1 == m:
            start = False
            break
        i, j = i + num * funcs[move][0], j + num * funcs[move][1]
        move = (move + 1) % 4
        m += 1
    num += 1

print(i, j)
