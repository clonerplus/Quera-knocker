#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:28:00 2021

@author: clonerplus
"""

def ip_mkr(ip, y):
    global trip, trips
    if y == 1:
        if ip == '' or len(ip) > 3 or int(ip) > 255 or len(ip) != len(str(int(ip))):
            return
        trip+=ip
        trips.append(trip)
        return
    for i in range(1, 4):
        a = trip
        if ip[:i] == '' or int(ip[:i]) > 255 or len(ip[:i]) != len(str(int(ip[:i]))) :
            continue
        trip+=ip[:i]+'.'
        ip_mkr(ip[i:], y-1)
        trip = a


trip = ''
trips = []

ip_mkr(input(), 4)
if trips != []: 
    for i in trips: 
        print(i)