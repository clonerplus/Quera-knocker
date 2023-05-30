#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:45:20 2021

@author: clonerplus
"""

class copy:
    def __init__(self, a):
        global string
        for i in range(len(a[::-1])):
            if a[i] == ' ':
                b = i
                break
        num = int(a[b+1:])
        key = a[:b]
        c = key * num
        string = c + string[len(c):]
        self.string = string

class compare:
    def __init__(self, a):
        global string, goodness
        if string == a:
            goodness += 1

class substr:
    def __init__(self, a):
        global string, goodness
        num = 0
        string1 = string
        for i in range(len(a)):
            if a[i] == ' ':
                num = int(a[i+1:])
                key = a[:i]
                break
        while key in string1 and num > 0:
            b = 0
            mun = num
            for i in range(len(string1[::len(key)])):
                b += len(key)
                if key == string1[b-len(key):b]:
                    if key not in string1[b-(2*len(key)):b-1]:
                        string1 = string1[b-len(key)+1:]
                        num-=1
            if num == mun:
                if key in string1[:len(key)]:
                    num-=1
                string1 = string1[1:]
        if num == 0:
            goodness+=1

class attach:
    def __init__(self, a):
        global string, goodness
        string1 = string
        t = 0
        b = 0
        for i in range(len(a)):
            if a[i] == ' ' and t==1:
                count = int(a[b+1:i])
                str = a[i+1:]
                break
            if a[i] == ' ' and t==0:
                key = a[:i]
                t = 1
                b=i
        key = key + str
        while key in string1 and count > 0:
            index = string1.index(key)
            string1 = string1[:index]+string1[index+len(key):]
            count-=1
        if count == 0:
            goodness+=1
        
class length:
    def __init__(self, a):
        global string, goodness
        if len(string) == int(a):
            goodness+=1

goodness = 0
eyval = 0                
string = input()
a = input()
eyval+=1

while a != 'Is it right or not?':
    if a[:4] == 'copy':
        a = copy(a[5:])
    elif a[:7] == 'compare':
        a = compare(a[8:])
    elif a[:6] == 'substr':
        a = substr(a[7:])
    elif a[:6] == 'attach':
        a = attach(a[7:])
    else:
        a = length(a[7:])
    a = input()
    eyval+=1

if (eyval-1)//2 <= goodness:
    print('Eyval')
else:
    print('HeifShod')

 
