# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:00:11 2015
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.
@author: Mychal
"""


def product_list(p):
    prod = 1
    while p:
        prod = prod * p.pop()
    return prod


# # alternatively
# def product_list(p):
#    prod = 1
#    for i in p:
#        prod = prod * i
#    return prod


print product_list([9])
print product_list([1,2,3,4])
print product_list([])    