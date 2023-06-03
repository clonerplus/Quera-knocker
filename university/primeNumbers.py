i, j = int(input()), int(input())
x, y = [], []
for e in range(i, j+1):
    y.append(e)
    if (e == 0) or (e == 1) or (e == 2):
        x.append(e)
    else:
        for b in range(2, e):
            if e % b == 0:
                x.append(e)
                break
for q in range(0, len(x)):
    if (x[q] != 2):
        for b in range(0, len(y)):
            if y[b] == x[q]:
                y.pop(b)
                break
for w in range (len(y)):
    print (y[w])

