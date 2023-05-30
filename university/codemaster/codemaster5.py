#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:52:02 2021

@author: clonerplus
"""

num = ''
result = []

def sym(x, y):
    global result, num
    if y == 1:
        for j in range(x):
            num+=str(j)
            result.append(num+num[::-1])
            for k in range(x):
                result.append(num+str(k)+num[::-1])
            num = num[:-1]
        return
    for j in range(x):
        num+=str(j)
        sym(x, y-1)
        num = num[:-1]

nk = input().split()
        

for j in range(2, int(nk[0])):
    result.append(str(j))

for j in range(1, int(nk[1])):
    num+=str(j)
    result.append(num+num[::-1])
    for k in range(2):
        result.append(num+str(k)+num[::-1])
    num = num[:-1]
for j in range(1, int(nk[1])):
    num+=str(j)
    sym(int(nk[1]), 1)
    num = num[:-1]
        
            