# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:04:11 2015
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.
@author: Mychal
"""


def product_list(list_of_numbers):
    prod = 1
    while list_of_numbers:
        prod = prod * list_of_numbers.pop()
    return prod

# # alternatively
# def product_list(list_of_numbers):
#    prod = 1
#    for i in list_of_numbers:
#        prod = prod * i
#    return prod

print product_list([9])
print product_list([1, 2, 3, 4])
print product_list([])
