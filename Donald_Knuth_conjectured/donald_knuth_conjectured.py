#!/usr/bin/env python
# coding: utf-8

import math


class Conjectured:
    
    def __init__(self, value, target):
        self.value = value
        self.target = target
        
        # action list
        self.actions = ["factorial", "square_root", "floor"]
        self.BFS()
        
        
    def operation(self, op, value):
        # If the value is larger than 100, the factorial operation will be skiped
        # If the value is not integer, the factorial operation will be skiped
        if value > 100 and op == 0:
            return value
        if not isinstance(value, int) and op == 0:
            return value
        
        # Three operations
        if op == 0:
            return math.factorial(value)
        elif op == 1:
            return math.sqrt(value)
        elif op == 2:
            return math.floor(value)
        
    # BFS
    def BFS(self):
        
        # level is the height of the BFS Tree
        # level 0 is root which has been skipped
        level = 1
        
        # This dict is used to store all the values for each level
        # e.g., level_dict = {1:[24,2.0,4]}
        level_dict = {}
        
        # This array is used to store opreration squence. 
        # It's the output
        actions_queue = []
        
        # The Maximum value of level is 29 
        while level < 30:
            
            if level not in level_dict:
                level_dict[level] = []
            
            # for each level, there are 3 to power of level nodes
            # for each non-leaf node, it has three childs (three actions)
            nums_node = pow(3,level)
            
            # This array is used to store the operations in each level
            operations = []
            
            # e.g., level 1: operations=[0, 1, 2]
            for x in range(nums_node):
                operations.append(x%3)
            
            for c, x in enumerate(operations):
                
                if level == 1:
                    out = self.operation(x, self.value)
                else:
                    value = level_dict[level-1][c//3] 
                    out = self.operation(x, value)
                
                if out == self.target:
                    # Get the operation squence
                    while c > -1 and level > 0:
                        ope = c %3
                        c = c//3
                        level -= 1
                        actions_queue.append(self.actions[ope])
                    
                    print(actions_queue[::-1])
                    return actions_queue[::-1]
                
                level_dict[level].append(out)
            
            level += 1           


Conjectured(4,5)




