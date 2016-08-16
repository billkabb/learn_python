# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:26:13 2016

@author: billkabb
"""
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n # ayto prepei na ginei return 1
   else:
      return n * f(n-1)