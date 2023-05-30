import numpy as np

Vx, Vy, Y0, h = [float(i) for i in input().split()]

coeffs = [-5, Vy, Y0-h]

l = np.roots(coeffs)
if np.iscomplex(l[0]):
    print("impossible")
    exit(0)

ll = [round(l[0], ndigits=2), round(l[1], ndigits=2)]


if len(ll) == 2:
    if ll[0] == ll[1]:
        if ll[0] * Vx < 0:
            print("impossible")
        else:
            print("%.2f" % (ll[0] * Vx))
    else:
        t = True
        if ll[1] * Vx > 0:
            print("%.2f" % (ll[1] * Vx))
            t = False
        if ll[0] * Vx > 0:
            print("%.2f" % (ll[0] * Vx))
            t = False
        if t:
            print("impossible")

elif len(ll) == 1:
    if ll[0] * Vx < 0:
        print("impossible")
    else:
        print("%.2f" % (ll[0] * Vx))
