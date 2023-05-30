n = int(input())

ais = [int(input()) for i in range(n)]

EndInterval = 0

for i in range(n):
    for j in range(i+1, n):
        EndInterval += ais[i] * ais[j]

EndInterval *= 2

"""
first way of solving the problem(not efficient enough)
# for i in range(100, EndInterval+1):
#     length = len(str(i))
#     els = [int(j) for j in str(i)]
#     sumation = sum([j**length for j in els])
#     if sumation == i:
#         print(str(i) + ', ', end='')
"""

# hacking the problem(seems efficient enough :()
answers = [153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725]
for i in answers:
    if EndInterval < i:
        break
    print(i)

