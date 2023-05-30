n, m = [int(input()) for i in range(2)]

result = 0

for i in range(-10, m+1):
    for j in range(1, n+1):
        result += int(((i+j)**3)/(j**2))

print(result)

