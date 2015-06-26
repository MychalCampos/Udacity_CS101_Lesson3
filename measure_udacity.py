# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:35:29 2015

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

@author: Mychal
"""


def measure_udacity(p):
    count = 0
    for i in p:
        if i.find('U') != -1:
            count = count + 1
    return count


def test():
    assert measure_udacity(['Dave', 'Sebastian', 'Katy']) == 0
    assert measure_udacity(['Umika', 'Umberto']) == 2
    print "All Test Cases Passed!"

test()
