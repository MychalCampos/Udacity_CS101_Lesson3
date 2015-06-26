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


def find_element(p, t):
    i = - 1
    m = 1
    for e in p:
        if e == t:
            i = i + m
        else:
            m = m + 1
    return i


def test():
    assert find_element([1, 2, 3], 3) == 2
    assert find_element(['alpha', 'beta'], 'gamma') == -1
    print "All Test Cases Passed!"

test()
