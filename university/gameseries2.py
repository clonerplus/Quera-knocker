#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 00:41:51 2021

@author: ClonerPlus
"""

n = int(input())
list1 = [[1], []]
list2 = []
list3 = []
a = 2
if n == 1:
    for i in list1:
        print('{', end=' ')
        for j in i:
            print(j, end=' ')
        print('}')
else:
    while n > 1:
        for i in list1:
            list2.append(i + [a])
        for i in range(len(list1)):
            list3.append(list2[i])
            list3.append(list1[i])
        list1 = list3[:]
        list2 = []
        list3 = []
        n -= 1
        a += 1
    print('{', end=' ')
    print(' }\n{ '.join(' '.join(map(str, i)) for i in list1), end='')
    print('}')
