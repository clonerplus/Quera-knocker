#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:19:40 2021

@author: clonerplus
"""

import sys

def highestPowerof2(n):
	if (n < 1):
		return 0

	res = 1

	for i in range(8*sys.getsizeof(n)):
	
		curr = 1 << i


		if (curr > n):
			break

		res = curr

	return res

def tile_mngr(mn):
    global tiles
    m, n = int(mn[0]), int(mn[1])
    if m == 0:
        return
    if m == 1:
        if 1 in tiles:
            tiles[1]+=n
        else:
            tiles[1] = n
        return
    a = highestPowerof2(m)
    b = n//a
    
    if m-a == n-(b*a):
        tile_mngr([m-a, b*a+m])
    else:
        tile_mngr([m-a, b*a])
        tile_mngr([n-(b*a), m])
    if a in tiles:
        tiles[a]+=b
    else:
        tiles[a] = b
    

tiles = {}

tile_mngr(sorted(int(i) for i in input().split()))

for i in sorted(list(tiles.items()), key=lambda x: -x[0]):
    print(i[1], '%s*%s tiles'%(i[0], i[0]))
