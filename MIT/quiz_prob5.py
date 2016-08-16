# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:16:53 2016

@author: billkabb
"""
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    b=0
    b1=0
    for i in range(len(listA)):
        b=listA[i]*listB[i]
        b1+=b
    return b1
    
listA = [1, 2, 3]
listB = [4, 5, 6]
print dotProduct(listA, listB)