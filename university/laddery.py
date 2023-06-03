#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:07:58 2022

@author: clonerplus
"""


def GCD(m, n):
    if n == 0:
        return m

    while m % n != 0:  # finds GCD

        rem = m % n
        m = n
        n = rem

    return abs(n)


m, n = sorted([int(input()), int(input())])

print(GCD(n, m))

