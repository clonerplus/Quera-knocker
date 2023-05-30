#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 17:38:27 2021

@author: clonerplus
"""
from collections import Counter
n = input()
m = input()
intlist = [int(i) for i in m.split()]
intdic = Counter(intlist)
result = 0
for i in intdic:
    if i+1 in intdic:
        result += intdic[i] * intdic[i+1]
print(result)