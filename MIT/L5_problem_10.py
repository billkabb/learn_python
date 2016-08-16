# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:34:43 2016

@author: billkabb
"""

def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    #numCalls = 0   this is the wrong line
    for i in range(n+1):
        numCalls = 0  # this is the solution
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFib(10)