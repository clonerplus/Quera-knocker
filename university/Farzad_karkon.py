n = int(input())
days = [int(i) for i in input().split()]
profit = 0

for i in range(1, n+1):
    for j in range(n-i+1):
        # print(days[j:j+i], end='')
        sums = sum(days[j:j+i])
        if profit < sums:
            profit = sums
    # print()
print(profit)

