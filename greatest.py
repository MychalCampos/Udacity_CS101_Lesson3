# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:05:04 2015
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.
@author: Mychal
"""


# # first attempt
# def greatest(p):
#    if len(p) > 0:
#        g = p[0]
#        for i in p:
#            if i > g:
#                g = i
#        return g
#    return 0


# more efficient
def greatest(p):
    g = 0
    for i in p:
        if i > g:
            g = i
    return g


print greatest([4, 23, 1])
print greatest([])