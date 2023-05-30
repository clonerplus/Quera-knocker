def prime_num_list(lim):
    l = [2, 3]
    it = 4
    while it**2 < lim:
        is_prime = True
        for prime in l:
            if not it % prime:
                is_prime = False
                break
        if is_prime:
            l.append(it)
        it += 1

    return l


if __name__ == "__main__":
    a, b = [int(input()) for i in range(2)]
    result = ""
    prime_list = prime_num_list(b)

    for i in prime_list:
        if a < i < b:
            result += str(i) + ","

    for i in range(a+1, b):
        is_prime = True
        for j in prime_list:
            if not i % j:
                is_prime = False
        if is_prime:
            result += str(i) + ","
    print(result[:-1])
    # print(prime_num_list(b))



