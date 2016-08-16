# -*- coding: utf-8 -*-
"""
Created on Sat May 21 03:14:33 2016

@author: billkabb
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    char = char.lower()
    aStr = ''.join(sorted(aStr.lower()))

    if len(aStr)<=1:
        if char == aStr:
            return True
        else:
            return False
    elif len(aStr) % 2 == 0:
        if char < aStr[len(aStr)/2]:
            aStr = aStr[:len(aStr)/2]
            return isIn(char, aStr)
            #if char == isIn(char, aStr[:len(aStr)/2]):

            #    return 'even'
        else:
            aStr = aStr[len(aStr)/2:]
            return isIn(char, aStr)

    elif len(aStr) % 2 == 1:
        if char == aStr[(len(aStr)/2)]:
            #print aStr[:(1+len(aStr)/2)]
            return True
        elif char < aStr[1+len(aStr)/2]:
             aStr = aStr[:(len(aStr)/2)]
             return isIn(char, aStr)

        elif char > aStr[(len(aStr)/2):]:
            aStr = aStr[(1+len(aStr)/2):]
            return isIn(char, aStr)

print isIn("a", 'abcdfeghijklmnop')

###############
### ~ MIT ~ ###
###############

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string

   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the
   #   test character
   midIndex = len(aStr)/2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True

   # Recursive case: If the test character is smaller than the middle
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])