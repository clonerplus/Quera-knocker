n = int(input())

fib = [1, 2]

while fib[-1] < n:
    fib.append(fib[-1]+fib[-2])


while n > 0:
    for i in range(len(fib)):
        if fib[i] > n:
            n -= fib[i-1]
            print(i, end=' ')
            break
        elif fib[i] == n:
            n -= fib[i]
            print(i+1, end=' ')
            break

