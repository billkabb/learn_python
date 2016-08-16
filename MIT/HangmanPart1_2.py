# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 03:04:33 2016

@author: billkabb
"""


def getGuessedWord(secretWord, lettersGuessed):
    tempWord = ""
    for i in secretWord:
        
        
        if i not in lettersGuessed:

            tempWord += "_ "

        else:
            tempWord += i
    return tempWord     
    
    
    
    
    
    
#secretWord = 'apple'
#lettersGuessed = ['i', 'a', 'u', 'k', 'l', 's']

#print getGuessedWord(secretWord, lettersGuessed)
print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])