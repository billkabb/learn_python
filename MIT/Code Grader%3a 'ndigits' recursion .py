# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 06:36:25 2016

@author: billkabb
"""

"""
Write a function called ndigits, that takes an integer x 
(either positive or negative) as an argument. 
This function should return the number of digits in x.
"""
def ndigits(x):
    x=abs(x)
    
    if x<=9:
        return 1
    
    
    if x>=10:
        
        return ndigits(x/10)+1
    
    
    
    

print ndigits(0)    

"""
def ndigits(x):
    x=abs(x)
    
    if x<10:
        return 1
    
            
    return ndigits(x/10)+1
"""