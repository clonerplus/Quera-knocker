#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 17:38:27 2021

@author: clonerplus
"""

n = input()
m = input()
intlist = sorted([int(i) for i in m.split()])
intset1 = set(intlist)
intset2 = intset1.copy()
intset1.discard(intlist[-1])
result = 0
indx1 = 0
indx2 = 0
for i in intset1:
    if i+1 in intset2:
        indx1 = len(intlist) - intlist[::-1].index(i)
        intlist = intlist[indx1:]
        indx2 = len(intlist) - intlist[::-1].index(i+1)
        result += (indx1)*(indx2)
    else:
        intlist = intlist[len(intlist) - intlist[::-1].index(i):]
print(result)