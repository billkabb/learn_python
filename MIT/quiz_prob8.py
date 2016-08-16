# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:16:53 2016

@author: billkabb
"""
def run_satisfiesF(L, satisfiesF):
    print ""


def satisfiesF(L):

    copyL = L[:]

    
    for i in copyL:
        if f(i)==False:
            L.remove(i)
    
    return len(L)

# For testing only, remove before submitting
def f(s):
    return 'a' in s

# Testing values, comment out before submitting
L = ['a', 'b', 'a']
print satisfiesF(L)
print L


#run_satisfiesF(L, satisfiesF)