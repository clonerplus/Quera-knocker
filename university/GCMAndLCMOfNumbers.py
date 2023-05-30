#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:07:58 2022

@author: clonerplus
"""

def GCD_LCM(m, n):
    
    m2, n2 = m, n
    
    while (m%n != 0): # finds GCD
        
        rem = m % n
        m = n
        n = rem
    
    
    m2 /= n           # finds LCM
    n2 /= n
    
    return n, int(m2*n2*n)
        


m, n = input().split()
m, n = int(m), int(n)

if m >= n: print(*GCD_LCM(m, n), sep=' ')

else: print(*GCD_LCM(n, m), sep=' ')
