# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 01:31:40 2016

@author: billkabb
"""

"""
 Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

Assume that

testList = [1, -4, 8, -9]

For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.

Example Question:

>>> print testList
[5, -20, 40, -45]

Solution to Example Question

  >>> print testList
  [1, 4, 8, 9]

"""
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def absNum(a):
    return abs(a)
    
applyToEach(testList, absNum)

print testList

####################
# [2, -3, 9, -8] #

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def absNum(a):
    return a+1
    
applyToEach(testList, absNum)

print testList

####################
# [1, 16, 64, 81] #

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def absNum(a):
    return a*a
    
applyToEach(testList, absNum)

print testList




