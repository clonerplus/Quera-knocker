#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 09:42:28 2022

@author: clonerplus
"""

global DOMINO_NEEDED

n = int(input())

row = [0 for i in range(n)]

a = [row[:] for i in range(3)]

counter = 1

DOMINO_NEEDED = n/2 * 3

def completedRecDuplicateFinder():
    pass
    

def verticalRec(a, x, y, counter):
    
    try:
        if a[y+1][x] == 0:
            a[y][x] = a[y+1][x] = counter
        
            return True
    except:
        
        return False

def horizontalRec(a, x, y, counter):
    
    try:
        if a[y][x+1] == 0:
            a[y][x] = a[y][x+1] = counter
        
            return True
    except:
        
        return False
    

def recursiveRecFiller(a, counter):
    
    global DOMINO_NEEDED
    
    if counter == DOMINO_NEEDED + 1:
        print(a)
        return
    
    for j in range(len(a)):
        for i in range(len(a[0])):
            
            if a[j][i] == 0:
                
                if verticalRec(a, i, j, counter):
                    recursiveRecFiller(a, counter+1)
                    a[j][i] = a[j+1][i] = 0
                
                elif horizontalRec(a, i, j, counter):
                    recursiveRecFiller(a, counter+1)
                    a[j][i] = a[j][i+1] = 0
    

        

recursiveRecFiller(a, counter)
                    
    