#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 22:45:12 2021

@author: clonerplus
"""

def printer(x):
    if len(x) == 1:
        print('%i:'%int(x), int(x)*x)
        return
    printer(x[:-1])
    print('%i:'%int(x[-1]), int(x[-1])*x[-1])

printer(input())