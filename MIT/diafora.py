# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 04:24:16 2016

@author: billkabb
"""
# endiaferousa loopa
def foo(L):
    val = L[0]
    while (True):
        val = L[val]
        
a = [1, 2, 3, 4, 0]

print foo(a)

#####################