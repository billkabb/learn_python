# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 01:19:43 2016

@author: billkabb
"""
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

#print f(5)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    
    
    s = 0
    
    rad = 0
    while start < stop:
        s = f(start)*step
        rad = s+rad
        #print s2
        
        start+=step
    return rad  
         
        
        
print  radiationExposure(40, 100, 1.5)  