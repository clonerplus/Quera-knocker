n = int(input())
results = []

for i in range(n):
    name = input().lower()
    new_name = name[0].upper()
    q = False
    for j in range(1, len(name)):
        if q:
            new_name += name[j].upper()
            q = False
            continue
        q = False
        if j != len(name)-1 and name[j] == ' ':
            q = True
        new_name += name[j]

    results.append(new_name)

print('\n'.join(map(str, (i for i in results))))

