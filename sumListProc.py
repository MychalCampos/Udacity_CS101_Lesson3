# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:03:36 2015
Using simple for loop to sum all elements of a list
@author: Mychal
"""


def sum_list(p):
    total = 0
    for i in p:
        total = total + i
    return total


# test cases
def test():
    assert sum_list([1, 7, 4]) == 12
    assert sum_list([9, 4, 10]) == 23
    assert sum_list([44, 14, 76]) == 134
    print "All Test Cases Passed!"

test()
