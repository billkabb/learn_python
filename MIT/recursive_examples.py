# -*- coding: utf-8 -*-
"""
Created on Sat May 21 03:14:33 2016

@author: billkabb
"""
#explode('hello') -> 'h e l l o'
def explode(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])
print explode('hello')

print '#####'
#removeDublicates ('aabbcc') -> 'abc'

def removeDups(word):
    if len(word) <= 1:
        return word
    elif word[0]==word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])

print removeDups('aabbcc')
print '#####'

#reverse string
def reverseStr(inputString):
    # "hello"
    # take the last character
    #   "o" + reverseStr("hell")
    #       "l" + reverseStr("hel")
    #           "l" + reverseStr("he")
    #               "e" + reverseStr("h")
    #                   "h" + reverseStr("")
    if len(inputString) == 0:
        return ""
    outputStr = inputString[-1] + reverseStr(inputString[:-1])
    return outputStr

print reverseStr("hello")
print '#####'

# Power calculation
def power(x, n):
    # x^n = x * x^(n-1)
    # x^3 = x * x^2
    #           x * x^1
    #               x * x^0
    if n==0:
        return 1
    output = x * power(x, n-1)
    return output

print power(4, 4)
print '#####'
##https://www.youtube.com/watch?v=M9dvNkSu2LY min : 8.25
