t = int(input())
results = []

for i in range(t):
    goals = input().split(' ')
    goals = [int(j) for j in goals]
    if goals[0] + goals[2] > goals[1] + goals[3]:
        results.append("perspolis")
    elif goals[0] + goals[2] < goals[1] + goals[3]:
        results.append("esteghlal")

    else:
        if goals[1] > goals[2]:
            results.append("esteghlal")
        elif goals[1] < goals[2]:
            results.append("perspolis")
        else:
            results.append("penalty")

for i in results:
    print(i)

