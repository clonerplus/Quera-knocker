n = int(input())

mat = [[] for i in range(n)]

for i in range(n):
    mat[i] = [int(i) for i in input().split()]

result = 0
s = 0
for j in range(n):
    s += mat[0][j]
    if int(s ** 0.5) ** 2 == s:
        result += 1

funcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
i, j = 0, n-1
funci = 0
seen = n
a = n-1
while a > 0:
    for _ in range(2):
        funci = (funci + 1) % 4
        for __ in range(a):
            i, j = i + funcs[funci][0], j + funcs[funci][1]
            s += mat[i][j]
            if int(s ** 0.5) ** 2 == s:
                result += 1
            seen += 1
    a -= 1

print(result)
