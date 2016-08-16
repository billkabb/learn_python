# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:16:53 2016

@author: billkabb
"""
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList==[]: 
        return []
    if type(aList) != list: 
        return [aList]
    else:
        return flatten(aList[0])+flatten(aList[1:])