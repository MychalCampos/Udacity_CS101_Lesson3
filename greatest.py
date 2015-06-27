# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:11:18 2015
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.
@author: Mychal
"""


def greatest(p):
    g = 0
    for i in p:
        if i > g:
            g = i
    return g
    
    
print greatest([4, 23, 1])
print greatest([])
