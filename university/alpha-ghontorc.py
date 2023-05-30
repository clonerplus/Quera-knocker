#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 17:03:12 2021

@author: clonerplus
"""

def b_c(b, n):
    hel = 'ABCDEFG'
    result = ''
    while n>=b:
        rem = n % b
        n = n // b
        if rem > 9:
            result += hel[rem-10]
        else:
            result += str(rem)
    
    if n%b > 9:
        result+=hel[n%b-10]
    else:
        result+=str(n%b)
    return result[::-1]
        

a = input()
b, n = int(a[-2:]), int(a[:-2])
print(b_c(b, n))
