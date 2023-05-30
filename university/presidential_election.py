n = int(input())
prtcipnts = [i+1 for i in range(n)]

indx = 1
termined = 0
j = 0
while len(prtcipnts) > 1:
    n_prtcipnts = []
    for i in range(j, len(prtcipnts), 2):
        n_prtcipnts.append(prtcipnts[i])

    j = 0
    if i == len(prtcipnts)-1:
        j = 1

    prtcipnts = n_prtcipnts.copy()

print(*prtcipnts)
