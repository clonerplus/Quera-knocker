#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:21:21 2022

@author: clonerplus
"""

import math

global valuesList

def constrainChecker(nodes, neighbours, currentNode, values): # checks the rules to the nodes
    
    
    if nodes[currentNode] == "T": # if the shape is Triangle
    
        multipliedNeighbourNodes = 1
        
        for i in neighbours:
            multipliedNeighbourNodes *= values[i]
        
        
        if (values[currentNode] == 
            multipliedNeighbourNodes // 
            (10**int(math.log10(multipliedNeighbourNodes)))):
            
            return True
            
        
    elif nodes[currentNode] == "S": # if the shape is Square
        
        multipliedNeighbourNodes = 1
        
        for i in neighbours:
            multipliedNeighbourNodes *= values[i]
            
            
        if (values[currentNode] ==
            multipliedNeighbourNodes % 10):
                
            return True
    
    
    elif nodes[currentNode] == "P": # id the shape is Pentagon
          
        sumedNeighbourNodes = 0
        
        for i in neighbours:
            sumedNeighbourNodes += values[i]
            

        if (values[currentNode] == 
            sumedNeighbourNodes // 
            (10**int(math.log10(sumedNeighbourNodes)))):
            

            return True
        
    
    else : # node should be equal to Hexagon
      
        sumedNeighbourNodes = 0
        
        for i in neighbours:
            sumedNeighbourNodes += values[i]
            

        if (values[currentNode] == 
            sumedNeighbourNodes % 10):
            
            return True
    
    
    return False
    
    
def currentValueValidator(neighbours, values, nodesChecked, currentNode): # checks the node's value to make sure to this value there is no conflict
    
    for i in range(currentNode+1):
                
        if nodesChecked[i] == False:
            doesEveryNeighbourHaveValue = True
            
            for j in neighbours[i]:
                
                if values[j] == 0:
                    doesEveryNeighbourHaveValue = False
                    break
            
            if doesEveryNeighbourHaveValue:
                
                if constrainChecker(nodes, neighbours[i], i, values):
                    nodesChecked[i] = True
                
                else:
                    return []
    
    return nodesChecked
    
        

def nodeByNodeTracker(nodes, neighbours, values, possibleValues, currentNode, nodesChecked):
    
    if currentNode == len(nodes): # no more nodes to check % THE VALUES LIST IS COMPELETE %
        
        for i in range(len(nodesChecked)): # checks if each node value meets the constrain of the problem
            if nodesChecked[i] == False:
                if not constrainChecker(nodes, neighbours[i], i, values): # if it isn't what we wanted
                    return False 
            
        valuesList.append(values) # holds final values
        
        
        return True
    
    currentValue = 0 # starting point of testing a number for a node
    
    originalNodesChecked = nodesChecked[::] # saves the nodesChecked from last function call

    
    while currentValue != 9: # while there is value to check for this set of values
        
        values[currentNode] = possibleValues[currentValue]
                
        nodesChecked = currentValueValidator(neighbours, values, nodesChecked, currentNode)
        
        if nodesChecked != []:
            
            if nodeByNodeTracker(nodes, neighbours, values, possibleValues, currentNode+1, nodesChecked):
                
                return True
                    

            
        
        
        currentValue += 1
        
        nodesChecked = originalNodesChecked[::]
    
    # print(values)
    values[currentNode] = 0
    

def requirementDefiner(nodes, neighbours): # defines and prepares basic requirements for each test and starts the nodeByNodeTracker
    
    values = [0 for i in range(len(nodes))]
    possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nodesChecked = [False for i in range(len(nodes))]
    for i in range(len(nodes)):
        if nodes[i] == 'C':
            nodesChecked[i] = True
    

    
    currentNode = 0

    nodeByNodeTracker(nodes, neighbours, values, possibleValues, currentNode, nodesChecked)

    
    
    




n = int(input()) # times to operate

valuesList = []

for i in range(n):
    
    E, V = [int(x) for x in input().split()] # E = nodes, V = vertices
    
    nodes = input().split() # stores shape of every node
    
    nodeNeighbours = [[] for j in range(E)] # stores node neighbours
    
    for j in range(V):
        
        start, end = [int(y) for y in input().split()] # gets and stores vertice's start and end
        
        nodeNeighbours[start].append(end)
        nodeNeighbours[end].append(start)
            
    requirementDefiner(nodes, nodeNeighbours) # starting the process for any input

# n = 1
# E, V = 9, 8
# nodes = ['C', 'P', 'H', 'S', 'S', 'H', 'H', 'T', 'C']
# nodeNeighbours = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7]]  
# requirementDefiner(nodes, nodeNeighbours)
# n = 2
# E, V = 7, 6
# nodes = ['P', 'T', 'T', 'H', 'P', 'T', 'T']
# nodeNeighbours = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5]]
# requirementDefiner(nodes, nodeNeighbours)
# n = 1
# E, V = 10, 9
# nodes = ['H', 'P', 'T', 'H', 'C', 'S', 'T', 'S', 'P', 'C']
# nodeNeighbours = [[2], [8,9], [0,3,4,5,8], [2], [2], [2,7], [8], [5], [1,2,6], [1]]
# requirementDefiner(nodes, nodeNeighbours)

print('\n'.join(' '.join(map(str, i)) for i in valuesList)) # printouts the result
