#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:19:40 2021

@author: clonerplus
"""

class Q:
    def __init__(self):
        a = input()
        self.b = [int(i) for i in input().split()]
    def sub_adder(x):
        Sum = 0
        a = len(x)
        for i in range(1, a+1):
            Sum += (x[i-1])*(a+1-i)*i
        print(Sum)

q = Q()
Q.sub_adder(q.b)