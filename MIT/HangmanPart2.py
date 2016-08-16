# -*- coding: utf-8 -*-
#from HangmanPart1 import isWordGuessed
#from HangmanPart1_2 import getGuessedWord
#from HangmanPart1_3 import getAvailableLetters
from ps3_hangman import loadWords
from ps3_hangman import chooseWord
from ps3_hangman import wordlist
import random
import string
###################################
def getGuessedWord(secretWord, lettersGuessed):
    
    for i in range(len(lettersGuessed)):
        #print lettersGuessed[i]
        if lettersGuessed[i] in secretWord:
            #print 'yes'
            secretWord = secretWord.replace(lettersGuessed[i], "_")
            #print secretWord
    
    return secretWord     
###################################
def getUnguessedWord(unSecretWord, secretWord, lettersGuessed):
    word=[]
    
    for s in range(len(secretWord)):
        #print s
        if secretWord[s] == "_":
            word.append(unSecretWord[s])
                
            #print wor
        elif secretWord[s] != "_":    
            word.append("_")
    #print  ' '.join(word)        
    return ' '.join(word)
      
###################################
def isWordGuessed( secretWord, lettersGuessed):
    #print lettersGuessed[5]
    for i in range(len(lettersGuessed)):
        #print lettersGuessed[i]
        if lettersGuessed[i] in secretWord:
            #print 'yes'
            secretWord = secretWord.replace(lettersGuessed[i], "")
            #print secretWord
    
    return secretWord == ""
##################################
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
        #if lettersGuessed[i] in secretWord:
            #print 'yes'
        alphabet = alphabet.replace(lettersGuessed[i], "")
            #print secretWord
    
    return alphabet     
####################################


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %i letters long." %len(secretWord)
    # FILL IN YOUR CODE HERE...
    #print "The secret word contains %i letters" %len(secretWord)
    #print "Please guess a letter: ",
    #guess = raw_input("Please guess a letter: ")
    #guessInLowerCase = guess.lower()
    lettersGuessed = []
    mistakesMade = 0
    guessLeft = 0
    #word=[]
    secretWord = str(secretWord)
    print secretWord
    #secretWordUnguessed =  
    while guessLeft < 2*len(secretWord):
        print "-------------"
        print "You have %i guesses left." % (2*len(secretWord)-guessLeft)
        print "Available letters: %s" % getAvailableLetters(lettersGuessed)
        #print len(secretWord)
        guess = raw_input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        #lettersGuessed.append(guess)
#        print guess
#        print getUnguessedWord(unSecretWord, getGuessedWord(secretWord, lettersGuessed), lettersGuessed)
#        print ' '.join(secretWord)  
#        print getGuessedWord(secretWord, lettersGuessed)
#        if getGuessedWord(secretWord, lettersGuessed) == ' '.join(secretWord) :
#            print "Congratulations, you won!"
        if guess not in getAvailableLetters(lettersGuessed):
            lettersGuessed.append(guess)
            print "Oops! You've already guessed that letter: %s" % getUnguessedWord(unSecretWord, getGuessedWord(secretWord, lettersGuessed), lettersGuessed)
            #print lettersGuessed            
            #lettersGuessed.append(guess)
            #guessLeft-=1
            
        if guess in getAvailableLetters(lettersGuessed):
            if guess in secretWord:
                lettersGuessed.append(guess)
                print "Good guess: %s" % getUnguessedWord(unSecretWord, getGuessedWord(secretWord, lettersGuessed), lettersGuessed)
                #print lettersGuessed
                if getUnguessedWord(unSecretWord, getGuessedWord(secretWord, lettersGuessed), lettersGuessed) == ' '.join(secretWord):
                    return "Congratulations, you won!"
                    
            if guess not in secretWord:
                lettersGuessed.append(guess)
                print "Oops! That letter is not in my word: %s" % getUnguessedWord(unSecretWord, getGuessedWord(secretWord, lettersGuessed), lettersGuessed)           
                #print lettersGuessed
                #lettersGuessed.append(guess)
            #print getGuessedWord(secretWord, lettersGuessed)
                            #print 'not in word'
            guessLeft+=1
        
    return "Sorry, you ran out of guesses. The word was else."    


#print chooseWord(wordlist)
#wordlist = loadWords()
#secretWord = chooseWord(wordlist)
#
#unSecretWord = secretWord
#print secretWord
##print unSecretWord
#print "Welcome to the game, Hangman!"
#print "I am thinking of a word that is %i letters long." %len(secretWord)

print hangman("sea")