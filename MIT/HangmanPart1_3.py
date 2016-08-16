# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 03:11:14 2016

@author: billkabb
"""
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase
    
    for i in range(len(lettersGuessed)):
        #print lettersGuessed[i]
        if lettersGuessed[i] in secretWord:
            #print 'yes'
            alphabet = alphabet.replace(lettersGuessed[i], "")
            #print secretWord
    
    return alphabet     
    
    
    
secretWord = 'apple'
#lettersGuessed = ['i', 'a', 'u', 'k', 'l', 's']

#print getAvailableLetters(lettersGuessed)