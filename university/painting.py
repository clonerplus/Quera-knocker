#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:38:01 2021

@author: clonerplus
"""
def gradient(x):
    global xylist, selected, jj
    a = selected[-1]
    return (a[2] - x[2]) / (a[1] - x[1]+.1**10)
def painting():
    global jj, selected, xylist
    nk = input()
    if 2**(int(nk.split()[1])+1)-1 > int(nk.split()[0]):
        print(-1)
        return
    xylist = []
    selected = []
    p = 1
    for i in range(int(nk.split()[0])):
        m = input()
        xylist.append([i] + [int(j) for j in m.split()])
    
    if 2**(int(nk.split()[1])+1)-1 < int(nk.split()[0]):
        xylist = sorted(xylist, key=lambda x: (-x[1],x[2]))
        selected = [i+[0] for i in xylist[2**(int(nk.split()[1])+1)-1:]]
        xylist = xylist[:2**(int(nk.split()[1])+1)-1]
    
    xylist = [xylist]
    nxylist = xylist
    for i in range(int(nk.split()[1])+1):
        xylist = nxylist
        nxylist = []
        for j in range(len(xylist)):
            jj = j
            xylist[j] = sorted(xylist[j], key=lambda x: (-x[1], x[2]))
            selected.append(xylist[j].pop(0)+[p])
            xylist[j] = sorted(xylist[j], key=gradient)
            lxy = len(xylist[j])//2
            nxylist.append(xylist[j][:lxy])
            nxylist.append(xylist[j][lxy:])
            p+=1
    
    
    print('\n'.join(str(i[-1]) for i in sorted(selected)))

painting()
