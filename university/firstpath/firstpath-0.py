#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 20:16:21 2021

@author: clonerplus
"""
import time
primelist = []

def prime(x):
    global primelist
    if x in primelist:
        return x
    if x == 1:
        return 0
    for i in range(1, 1+int(int(x) ** (1/2))):
        if x%i == 0:
            if x!=i and i!=1:
                return 0
    primelist.append(x)
    return x
n = int(input())
a = dict()
for i in range(n):
    a['test %i'%(i+1)] = []
    b = ''
    c = []
    d = []
    m = int(input())
    l = m
    for j in range(m+2):
        b = input().split()
        if l > 0:
            for k in b:
                c.append(prime(int(k)))
            a['test %i'%(i+1)].append(c)
            c = []
            l-=1
        else:
            d.append(tuple(int(k) for k in b))
    a['order %i'%(i+1)] = d
    
s=time.time()
for i in range(len(a)//2):
    first = a['order %i'%(i+1)][0]
    last = a['order %i'%(i+1)][1]
    r, c = first[0], first[1]
    a['test %i'%(i+1)][r][c] = 0
    text = ''
    q = 0
    while True:
        if q == 1:
            print('No Monaseb Masir!')
            break
        q = 1
        if (c+1)<len(a['test %i'%(i+1)]) and a['test %i'%(i+1)][r][c+1] != 0:
            text+='R'
            a['test %i'%(i+1)][r][c+1] = 0
            c+=1
            q = 0
            if (r, c) == last:
                break
        elif c>0 and a['test %i'%(i+1)][r][c-1] != 0:
            text+='L'
            a['test %i'%(i+1)][r][c-1] = 0
            c-=1
            q = 0
            if (r, c) == last:
                break
        elif (r+1)<len(a['test %i'%(i+1)]) and a['test %i'%(i+1)][r+1][c] != 0:
            text+='D'
            a['test %i'%(i+1)][r+1][c] = 0
            r+=1
            q = 0
            if (r, c) == last:
                break
        elif r>0 and a['test %i'%(i+1)][r-1][c] != 0:
            text+='U'
            a['test %i'%(i+1)][r-1][c] = 0
            r-=1
            q = 0
            if (r, c) == last:
                break
    if q == 0:
        print(text)
        
print(time.time()-s)        
  