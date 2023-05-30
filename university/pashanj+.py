#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:34:22 2021

@author: clonerplus
"""

n = input()
a = 0
num_g1 = input().split()
num_g2 = []
list = []

for i in range(len(num_g1)):
    if num_g1[i] not in num_g1[i+1:]:
        num_g2.append(num_g1[i])   

num_g1 = []

for i in range(len(num_g2)):
    for j in range(len(num_g2)):
        if i != j:
            num_g1.append([min(int(num_g2[i]),int(num_g2[j])), max(int(num_g2[i]),int(num_g2[j]))])

num_g2 = []

for i in range(len(num_g1)):
    if num_g1[i] not in num_g1[i+1:]:
        num_g2.append(num_g1[i])   

list = sorted(num_g2, key=lambda x:abs(int(x[0]) - int(x[1])))
for i in range(len(list)-1):
    if abs(list[i][0] - list[i][1]) != abs(list[i+1][0] - list[i+1][1]):
        list = list[:a] + sorted(list[a:i+1]) + list[i+1:]
        a=i+1
for i in list:
    print(i)