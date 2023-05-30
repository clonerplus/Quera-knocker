#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 23:05:53 2021

@author: clonerplus
"""

def lozenge(x):
    b = (x//2)
    c = []
    d = 1
    for i in range(1+x//2):
        a = b*(' ') + d*'*'+ b*(' ')
        print(a, end='')
        print(a)
        c.append(a)
        b-=1
        d+=2
    for i in c[:-1][::-1]:
        print(i, end='')
        print(i)
    
lozenge(int(input()))