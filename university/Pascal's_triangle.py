n = int(input())

l1 = [1, 1]
for i in range(n):
    if i == 0:
        print(1)
        continue

    if i == 1:
        print("1 1")
        continue

    l2 = [1]
    for j in range(len(l1) - 1):
        l2.append(l1[j] + l1[j + 1])
    l2.append(1)
    l1 = l2.copy()
    l2.clear()
    print(*l1)
