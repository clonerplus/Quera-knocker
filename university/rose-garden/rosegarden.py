#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 00:41:51 2021

@author: ClonerPlus
"""
nm = input()
n, m = int(nm[0]), int(nm[-2:])
r_l = ['B'] * n
for i in range(m):
    month = input()
    for j, k in enumerate(month):
        if k == 'W':
            if r_l[j] == 'B':
                r_l[j] = 'F'
            else:
                r_l[j] = 'B'
print(''.join(i for i in r_l), end='')
