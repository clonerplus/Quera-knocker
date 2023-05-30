import math

n = int(input())

points = [[] for i in range(n)]

for i in range(n):
    points[i] = [float(i) for i in input().split()]

no_one = True
# function y = x − [x]
t = True
for i in range(n):
    if abs(points[i][0] - math.floor(points[i][0]) - points[i][1]) > 0.2:
        t = False

if t:
    print(1)
    no_one = False

# function y = x**2 + x
t = True
for i in range(n):
    if abs(points[i][0]**2 + points[i][0] - points[i][1]) > 0.2:
        t = False

if t:
    print(2)
    no_one = False


# function y = ∣−x**3 + 1| + x**3
t = True
for i in range(n):
    if abs(abs(-points[i][0]**3 + 1) + points[i][0]**3 - points[i][1]) > 0.2:
        t = False

if t:
    print(3)
    no_one = False

if no_one:
    print("No ones")
