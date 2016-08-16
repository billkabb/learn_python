# -*- coding: utf-8 -*-
"""
Created on Sat May 21 03:14:33 2016

@author: billkabb
"""
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    a=0
    for i in aStr:
        #print a
        a+=1
    return a
print lenIter('billy')

######################################
# ~ MIT ~ ##
def lenIter(aStr):

    # Initialize a variable to hold our final count
    count = 0

    # Iterate over each character in the string, counting each one
    for char in aStr:
        count += 1
    return count