def get_prime_list(num, q):
    l = [2]
    it = 3
    while num > l[-1] or q != 0:
        is_prime = 1
        for i in range(len(l)):
            if it % l[i] == 0:
                is_prime = 0
                break
        if is_prime:
            l.append(it)
            if num < l[-1]:
                q -= 1
        it += 1
    print(l[-1])


n = input()
b = sum([int(i) for i in n])
get_prime_list(int(n), b)
