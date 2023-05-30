#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 02:11:42 2021

@author: clonerplus
"""
import time
primelist = []

def prime(x, a, b):
    global primelist
    if x in primelist:
        return(a, b)
    if x == 1:
        return
    for i in range(1, 1+int(int(x) ** (1/2))):
        if x%i == 0:
            if x!=i and i!=1:
                return
    primelist.append(x)
    return (a, b)
n = int(input())
a = dict()
for i in range(n):
    b = ''
    c = []
    d = []
    m = int(input())
    l = m
    for j in range(m+2):
        b = input().split()
        if l > 0:
            for k in range(len(b)):
                if prime(int(b[k]), m-l, k) != None:
                    c.append(prime(int(b[k]), m-l, k))
            l-=1
        else:
            d.append(tuple(int(k) for k in b))
    a['test %i'%(i+1)] = c
    a['order %i'%(i+1)] = d
s=time.time()

for i in range(len(a)//2):
    v = a['order %i'%(i+1)][0]
    index = a['test %i'%(i+1)].index(v)
    del a['test %i'%(i+1)][index]
    text = ''
    q = 0
    while v!=a['order %i'%(i+1)][1]:
        if q == 1:
            print('No Monaseb Masir!')
            break
        q = 1
        if index<len(a['test %i'%(i+1)]) and a['test %i'%(i+1)][index] == (v[0], v[1]+1):
            v = a['test %i'%(i+1)][index]
            text+='R'
            del a['test %i'%(i+1)][index]
            q=0
        elif index>0 and a['test %i'%(i+1)][index-1] == (v[0], v[1]-1):
            v = a['test %i'%(i+1)][index-1]
            text+='L'
            del a['test %i'%(i+1)][index-1]
            index-=1
            q=0
        else:
            try:
                index = a['test %i'%(i+1)].index((v[0]+1, v[1]))
                v = a['test %i'%(i+1)][index]
                text+='D'
                del a['test %i'%(i+1)][index]
                q=0
            except:
                pass
            try:
                index = a['test %i'%(i+1)].index((v[0]-1, v[1]))
                v = a['test %i'%(i+1)][index]
                text+='U'
                del a['test %i'%(i+1)][index]
                q=0
            except:
                pass
    if q==0:
        print(text)
print(s-time.time())
    