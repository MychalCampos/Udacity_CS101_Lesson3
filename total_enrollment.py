# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:29:27 2015
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string,
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).
@author: Mychal
"""


udacious_univs = [['Udacity', 90000, 0]]

usa_univs = [ ['California Institute of Technology', 2175, 37704],
              ['Harvard', 19627, 39849],
              ['Massachusetts Institute of Technology', 10566, 40732],
              ['Princeton', 7802, 37000],
              ['Rice', 5879, 35551],
              ['Stanford', 19535, 40569],
              ['Yale', 11701, 40500] ]


# # your original attempt
# def total_enrollment(p):
#    students, fees = 0, 0
#    for i in p:
#        students = students + i[1]
#        fees = fees + (i[1] * i[2])
#    return students, fees


# more efficient, based on solution set
def total_enrollment(p):
    students, fees = 0, 0  # initiate total number of students and total fees
    for name, enrollment, tuition in p:
        students = students + enrollment
        fees = fees + (enrollment * tuition)
    return students, fees
    
    
print total_enrollment(udacious_univs)
print total_enrollment(usa_univs)
