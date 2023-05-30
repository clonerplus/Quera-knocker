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


# s = time.time()
# for ii in range(len(a)//2):
#     path = []
#     v = a['order %i'%(ii+1)][0]
#     path.append(v)
#     del a['test %i'%(ii+1)][a['test %i'%(ii+1)].index(v)]
#     text = ''
#     nn = 1
#     while a['order %i'%(ii+1)][1] not in path:
#         if nn == 0:
#             print('No monaseb masir!')
#             break
#         nn = 0
#         for i, j in enumerate(a['test %i'%(ii+1)]):
#             f, g = v[0]-j[0], v[1]-j[1]
#             if f == 0:
#                 if g == 1:
#                     path.append(j)
#                     v = j
#                     del a['test %i'%(ii+1)][i]
#                     text+='L'
#                     nn = 1
#                     break
#                 elif g == -1:
#                     path.append(j)
#                     v = j
#                     del a['test %i'%(ii+1)][i]
#                     text+='R'
#                     nn = 1
#                     break
#             elif g == 0:
#                 if f == 1:
#                     path.append(j)
#                     v = j
#                     del a['test %i'%(ii+1)][i]
#                     text+='U'
#                     nn = 1
#                     break
#                 elif f == -1:
#                     path.append(j)
#                     v = j
#                     del a['test %i'%(ii+1)][i]
#                     text+='D'
#                     nn = 1
#                     break
#     if a['order %i'%(ii+1)][1] in path:
#         print(text)
                
                
# print(time.time()-s)             
                
                
                
                
                
                
                
        