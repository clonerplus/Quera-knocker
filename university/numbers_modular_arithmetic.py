a, b = [int(i) for i in input().split()]
c = max(a, b) - min(a, b)

for i in range(2, c+1):
    if c % i == 0:
        print(i, end=' ')


