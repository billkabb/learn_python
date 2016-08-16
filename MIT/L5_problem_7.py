# -*- coding: utf-8 -*-
"""
Created on Sat May 21 03:14:33 2016

@author: billkabb
"""
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    '''
    For this problem, write a recursive function,
    lenRecur, which computes the length of an input argument (a string),
    by counting up the number of characters in the string. 
    '''
    # Your code here

    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])
        

print lenRecur("billy")