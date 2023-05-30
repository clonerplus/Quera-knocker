a, b = input().split()
a, b = int(a), int(b)
result = ""

while a >= b:
    result += str(a % b)
    a //= b
result += str(a)

result = result[::-1]

sum1 = sum2 = 0
for i in range(0, len(result), 2):
    sum1 += int(result[i])

for i in range(1, len(result), 2):
    sum2 += int(result[i])

if sum1 == sum2:
    print("Yes")
    exit(0)
print("No")

