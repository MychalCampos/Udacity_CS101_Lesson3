# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:57:45 2015
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
@author: Mychal
"""


# using index function
def find_element(p, t):
    if t in p:
        return p.index(t)
    else:
        return -1


# # using index function and 'not in'
# def find_element(p, t):
#    if t not in p:
#        return -1
#    return p.index(t)


# # using for loop
# def find_element(p, t):
#    i = 0
#    for e in p:
#        if e == t:
#            return i
#        i = i + 1
#    return -1


# # using while loop
# def find_element(p, t):
#    i = 0
#    while i < len(p):
#        if p[i] == t:
#            return i
#        i = i + 1
#    return -1


def test():
    assert find_element([1, 2, 3], 3) == 2
    assert find_element(['alpha', 'beta'], 'gamma') == -1
    assert find_element(['CS101', 'CS373', 'CS212', 'CS101', 'CS373',
                         'CS262'], 'CS101') == 0
    print "All Test Cases Passed!"

test()
