#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 16:24:38 2021

@author: clonerplus
"""

def peekdepthfidr(ilist):
    if len(ilist) in {1, 2}:
        print('Yes')
        return
    maindx = len(ilist) - ilist[::-1].index(max(ilist))
    miindx = len(ilist) - ilist[::-1].index(min(ilist))
    if (ilist[:maindx] == sorted(ilist[:maindx])) and (ilist[maindx:][::-1] == sorted(ilist[maindx:])) and (len(ilist[maindx:]) == len(set(ilist[maindx:]))):
        print('Yes')
        return
    elif (ilist[:miindx][::-1] == sorted(ilist[:miindx])) and (ilist[miindx:] == sorted(ilist[miindx:])) and (len(ilist[miindx:]) == len(set(ilist[miindx:]))):
        print('Yes')
        return
    print('No')
    return
        
n = input()
m = input()
ilist = [int(i) for i in m.split()]
peekdepthfidr(ilist)