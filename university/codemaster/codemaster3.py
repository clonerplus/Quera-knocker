#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:27:08 2021

@author: clonerplus
"""
import time
def base_chng(b, n):
    hel = 'ABCDEFG'
    result = ''
    while n>=b:
        rem = n % b
        n = n // b
        if rem > 9:
            result += hel[rem-10]
        else:
            result += str(rem)
    rem = n % b
    if rem > 9:
        result+=hel[rem-10]
    else:
        result+=str(rem)
    if result == result[::-1]:
        print(result[::-1])
        return True

def prime(a, b):
    global primelist
    N = 0
    x = 3
    if b > 2:
        N+=1
    while N < a:
        if base_chng(b, x):
            N+=1
            for i in range(3, 1+int(x ** (1/2))):
                if x%i == 0:
                    N-=1
                    break
        x+=2
    print(x-2)

nk = input().split()
s = time.time()
prime(int(nk[0]), int(nk[1]))
print(time.time()-s)