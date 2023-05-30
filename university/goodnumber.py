#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:26:45 2021

@author: clonerplus
"""

def nicenum(x):
    if x == 1:
        print(1)
        return
    a = 1
    n = 2
    while True:
        N = 0
        a+=n
        b = int(a**.5)+1
        if int(a**.5) == a**.5:
            b-=1
        for i in range(1, b):
            if a%i == 0:
                N+=1
        N*=2
        if int(a**.5) == a**.5:
            N+=1
            
        if N >= x:
            print(a)
            break
        
        n+=1

nicenum(int(input()))
