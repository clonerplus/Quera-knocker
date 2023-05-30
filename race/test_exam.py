n = int(input())
answers = input()
k = int(input())

results = []

def give_index(ch):
    if ch == 'A':
        return 0
    if ch == 'B':
        return 1
    if ch == 'C':
        return 2
    if ch == 'D':
        return 3


for i in range(k):
    result = 0
    for j in range(n):
        q = input()
        true_index = give_index(answers[j])
        if q[true_index] == '#':
            if '#' not in q[:true_index] + q[true_index + 1:]:
                result += 3
            else:
                result += -1

        else:
            if '#' in q:
                result += -1

    results.append(result)

for i in results:
    print(i)

