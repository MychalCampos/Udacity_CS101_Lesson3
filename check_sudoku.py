# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:30:10 2015
# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.
@author: Mychal
"""


correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               

incorrect6 = [[2,2,2],
             [2,2,2],
             [2,2,2]]

incorrect7 = [[1,1,4,4], 
              [1,1,4,4], 
              [4,4,1,1], 
              [4,4,1,1]]

incorrect8 = [[1]]


# helper procedure for transposing a list
def transposeList(p):
    n = len(p)
    # initiate list
    tList = []
    i = 1
    while i <= n:
        tList.append([0] * n)
        i = i + 1
    for j in range(0, n):
        for k in range(0, n):
            tList[j][k] = p[k][j]
    return tList


# # first attempt (passes all tests, but this is UGLY!)
#def check_sudoku(p):
#    result = True
#    n = len(p)
#    tp = transposeList(p)
#    if n == len(tp) and n > 1:
#        i = 0
#        while i <= n - 1:  # check if any list elements are not integers
#            j = 0
#            while j <= n - 1:
#                if type(p[i][j]) != int:
#                    result = False
#                    break
#                    i = n - 1
#                else:
#                    j = j + 1
#            i = i + 1
#        if result:  # if all elements are integers
#            i = 0
#            while i <= n - 1:
#                if [sum(p[i]), sum(tp[i])] != [0.5*n*(n+1)]*2:
#                    result = False
#                    break
#                else:
#                    # this handles the case where a row or column has constant values
#                    # without this case, incorrect6 would pass the test
#                    if [p[i], tp[i]] == [[sum(p[i])*1.0/n] * n]*2:
#                        result = False
#                        break
#                    else:  # this handles the case where there are duplicate rows
#                        # without this case, incorrect7 would pass the test                    
#                        j = i + 1
#                        while j <= n-1:
#                            if p[i] == p[j] or tp[i] == tp[j]:
#                                result = False
#                                break
#                            else:
#                                j = j + 1
#                i = i + 1
#    return result


# this is cleaner and easier to understand
# instructor's solution
# here, we mechanically check for duplicate entries of an integer in each row 
# and each column (each list element is a column) OR if there is an entry that
# should not be in the sudoku square at all
def check_sudoku(p):
    n = len(p)
    digit = 1  # start with 1
    while digit <= n:  # go through each digit
        i = 0
        while i < n:  # go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n:  # for each entry in ith row/column
                if p[i][j] == digit:
                    row_count = row_count + 1  # check row count
                if p[j][i] == digit:
                    col_count = col_count + 1  # check col count
                j = j + 1
            # also accounts for cases where there are no instances of the digit            
            if row_count != 1 or col_count != 1:  
                return False  # if this holds, we're done!
            i = i + 1  # go to next row / column
        digit = digit + 1  # next digit
    return True


print check_sudoku(incorrect)
print check_sudoku(correct)
print check_sudoku(incorrect2)
print check_sudoku(incorrect3)
print check_sudoku(incorrect4)
print check_sudoku(incorrect5)
print check_sudoku(incorrect6)
print check_sudoku(incorrect7)
print check_sudoku(incorrect8)