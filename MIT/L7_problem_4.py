# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:26:13 2016

@author: billkabb
"""

def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      return set1[:1] + union(set1[1:], set2)
      
set1 = [1, 2, 3]
set2 = [3, 5, 6]

print union(set1, set2)