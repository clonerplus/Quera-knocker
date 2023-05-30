#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:27:08 2021

@author: clonerplus
"""
import math

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
    return result[::-1]

def prime(a, b):
    global primelist
    N = 0
    x = 2
    primelist = []
    while N < a:
        q = True
        for i in primelist[:int(len(primelist)**.5)+1]:
            if x%i == 0:
                q = False
                break
            # if i > x**(.5):
            #     break
        if q == True:
            primelist.append(x)
            ch_ed_x = base_chng(b, x)
            l = len(ch_ed_x)/2
            if ch_ed_x[:int(l)] == ch_ed_x[math.ceil(l):][::-1]:
                N+=1
                # print(x, ch_ed_x)
        x+=1
    print(x-1)

nk = input().split()
prime(int(nk[0]), int(nk[1]))