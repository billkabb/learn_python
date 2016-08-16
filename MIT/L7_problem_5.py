# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:26:13 2016

@author: billkabb
"""

def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count
      
x = 20
a = 5

print foo(x, a)