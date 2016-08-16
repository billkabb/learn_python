# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:16:53 2016

@author: billkabb
"""
def isPalindrome(aString):
    
    # Your code here
    a = aString
    if len(a) < 2:
        return True
    if a[0] != a[-1]:
        return False
    return isPalindrome(a[1:-1])
    
            
aString = "abcba"
print isPalindrome(aString)