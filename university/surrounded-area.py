#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:47:45 2021

@author: clonerplus
"""

def Rectangle(h):
    mxare, mini, minindx = 0, 0, 0
    h = [h]
    ii, g = [], []
    while len(h)>0:
        for i in h:
            if len(i) >= 1 and len(i)*max(i) > mxare:
                if len(i)*min(i) > mxare:
                    mxare = len(i)*min(i)
                if len(i) == 1:
                    continue
                mini = min(i)
                ii = i
                while mini in ii:
                    minindx = ii.index(mini)
                    g.append(ii[:minindx])
                    ii = ii[minindx+1:]
                g.append(ii)
        h.clear()
        h = g[:]
        g.clear()
    print(mxare)
    

n = input()
h = [int(i) for i in input().split()]
Rectangle(h)