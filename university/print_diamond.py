n = int(input())
n+=1

diam = 2*n+1

for i in range(n):
    print((2*n-(2*i+1))//2*' ', end='')
    print((2*i+1)*'*', end='')
    print((2*n-(2*i+1))//2*' ')

for i in range(1, n):
    print((2*n-(2*(n-i)-1))//2*' ', end='')
    print((2*(n-i)-1)*'*', end='')
    print((2*n-(2*(n-i)-1))//2*' ')

