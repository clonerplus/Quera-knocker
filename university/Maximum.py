n = int(input())
x = input().split()
f = 0
for a in range(n):
    if int(x[a]) > f:
        f = int(x[a])
print(f)

