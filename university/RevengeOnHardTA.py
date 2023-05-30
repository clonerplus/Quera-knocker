#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 00:34:58 2022

@author: clonerplus
"""


n = int(input())

F = [0 for i in range(25)] # stores values regarding each size of 3*n board
F[0] = 1
F[1] = 3

if (n % 2 != 0): # cannot be solved
    print(0)


else:
    
    for i in range(2, n//2+1): # has a formula that can be shown as 3*f(n-1) + 2(f(n-2)+f(n-3)+...+3+1)
        
        sumation = 0
        
        for j in range(0, n//2+1):
            sumation += 2*F[j]
            
        F[i] = sumation + F[i-1]
        
    
    print(2*F[n//2])    
