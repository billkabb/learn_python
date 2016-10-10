# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 02:39:01 2016

@author: billkabb
"""

gas_a= 50000 / 10
gas_b= 50000 / 50

print 15000+(gas_a * 4),30000+( gas_b * 4)

n = 10 
while n>1:
    print n
    if n%2 == 0:
        n = n/2
    else :
        n = 3*n+1