# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 02:32:39 2016

@author: billkabb
"""

def isWordGuessed( secretWord, lettersGuessed):
    #print lettersGuessed[5]
    for i in range(len(lettersGuessed)):
        #print lettersGuessed[i]
        if lettersGuessed[i] in secretWord:
            #print 'yes'
            secretWord = secretWord.replace(lettersGuessed[i], "")
            #print secretWord
    
    return secretWord == ""
    
    
    
#secretWord = 'apple'
#lettersGuessed = ['e', 'a', 'u', 'p', 'l', 's']

#print isWordGuessed(secretWord, lettersGuessed)