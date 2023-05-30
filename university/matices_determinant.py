import numpy

mat = numpy.array([[float(i) for i in input().split()] for i in range(int(input()))])

print("%.2f" % numpy.linalg.det(mat))
