def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


if __name__ == "__main__":

    a, b, c = [input() for i in range(3)]
    a = int(a, base=int(b))
    x = number_to_base(a, int(c))

    yes = True
    for i in range(len(x)//2):
        if x[i] != x[-1-i]:
            yes = False
            break
    if yes:
        print("YES")
    else:
        print("NO")


