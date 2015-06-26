# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:12:50 2015
# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.
@author: Mychal
"""


# helper procedure
def find_element(p, t):
    if t in p:
        return p.index(t)
    else:
        return -1


def union(a, b):
    for e in b:
        if find_element(a, e) == -1:
            a.append(e)
    return a

# test    
a = [1, 2, 3]
b = [2, 4, 6]
union(a,b)
print a
print b