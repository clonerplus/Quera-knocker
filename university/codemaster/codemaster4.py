#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:52:02 2021

@author: clonerplus
"""


def hole():
    global slctd, result, num
    resultx = []
    def cheq(l):
        global slctd
        for j in l:
            slctd.append(j)
            for i in range(2, 1+int(j ** (1/2))):
                if j%i == 0:
                    slctd.pop()
                    break
        return []
    
    def sym(x, y):
        global result, num
        if y == 1:
            for j in range(x):
                num+=str(j)
                result.append(int(num+num[::-1], x))
                resultx.append(num+num[::-1])
                for k in range(x):
                    result.append(int(num+str(k)+num[::-1], x))
                    resultx.append(num+str(k)+num[::-1])
                num = num[:-1]
            return
        for j in range(x):
            num+=str(j)
            sym(x, y-1)
            num = num[:-1]
    
    nk = input().split()
    n, k = int(nk[0]), int(nk[1])
            
    
    for j in range(2, k):
        result.append(j)
        resultx.append(str(j))
    result = cheq(result)
    if len(slctd) >= n:
        return
    
    for j in range(1, k):
        num+=str(j)
        result.append(int(num+num[::-1], k))
        resultx.append(num+num[::-1])
        for kj in range(2):
            result.append(int(num+str(kj)+num[::-1], k))
            resultx.append(num+str(kj)+num[::-1])
        num = num[:-1]
    
    result = cheq(result)
    
    N = 1
    while len(slctd) < n:
        for j in range(1, k):
            num+=str(j)
            sym(k, N)
            num = num[:-1]
        N+=1
        result = cheq(sorted(result))
    print(slctd[n-1])
        


num = ''
result = []
slctd = []
hole()       
            