#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 02:11:42 2021

@author: clonerplus
"""

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



for ii in range(len(a)//2):
    path = []
    v = a['order %i'%(ii+1)][0]
    vv = a['order %i'%(ii+1)][1]
    u = a['test %i'%(ii+1)].index(v)
    path.append(v)
    del a['test %i'%(ii+1)][a['test %i'%(ii+1)].index(v)]
    text = ''
    nn = 1
    while vv != path[-1]:
        if nn == 0:
            print('No monaseb masir!')
            break
        nn = 0
        if (v[0]-1, v[1]) in a['test %i'%(ii+1)]:
            text+='U'
            v = (v[0]-1, v[1])
            path.append(v)
            del a['test %i'%(ii+1)][a['test %i'%(ii+1)].index(v)]
            nn = 1
        elif (v[0]+1, v[1]) in a['test %i'%(ii+1)]:
            text+='D'
            v = (v[0]+1, v[1])
            path.append(v)
            del a['test %i'%(ii+1)][a['test %i'%(ii+1)].index(v)]
            nn = 1 
        elif (v[0], v[1]+1) == a['test %i'%(ii+1)][u]:
            text+='R'
            v = (v[0], v[1]+1)
            path.append(v)
            del a['test %i'%(ii+1)][a['test %i'%(ii+1)].index(v)]
            nn = 1
        elif (v[0], v[1]-1) == a['test %i'%(ii+1)][u-1]:
            text+='L'
            v = (v[0], v[1]-1)
            path.append(v)
            del a['test %i'%(ii+1)][a['test %i'%(ii+1)].index(v)]
            nn = 1
    if a['order %i'%(ii+1)][1] in path:
        print(text)       