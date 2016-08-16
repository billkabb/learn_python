# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:05:52 2016

@author: billkabb
"""
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    tempHand = hand.copy()
    try:    
        if word in wordList:
    
            if type(word) == str and len(word) > 0:
                for i in word:
                    tempHand[i]-=1
                    #print tempHand[i]
                return min(tempHand.values())>= 0
    except KeyError:
        return False 

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def calculateHandlen(hand):
    count = 0
    for i in hand:
        count += hand[i]
    return count	
def getWordScore(word, n):
    
    tempSum = 0
    for i in word:
        tempSum += SCRABBLE_LETTER_VALUES[i]
        #print SCRABBLE_LETTER_VALUES[i]

    #print tempSum
    tempSum = (tempSum * len(word))
    #print tempSum
    if len(word) == n:
        tempSum =  tempSum + 50
    return tempSum
def updateHand(hand, word):
 
    tempHand = hand.copy()
    for i in word:
        tempHand[i]-=1
        #print tempHand[i]
        if tempHand[i] == 0:
            del tempHand[i]
    return tempHand

# (end of helper code)
# -----------------------------------
#
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    tempScore = 0
    while calculateHandlen(hand):    
        tempHand = hand.copy() 
        #tempScore = 0
        listHand = []
        for i in tempHand:
            if tempHand[i]> 0:
                for j in range(tempHand[i]):
                    listHand.append(i)
            #print listHand
        
        print "Current Hand: %s" % ' '.join(listHand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        
        if word == ".":
            break        
        
        elif not isValidWord(word, hand, wordList):
            print "Ooops... Invalid word, please try again.\n"
            
        elif isValidWord(word, hand, wordList):
            tempScore += getWordScore(word, n)
            print "'%s' earned %i points. Total: %i points\n" % (word , getWordScore(word, n) , tempScore)
            hand = updateHand(hand, word)
    
    print "Goodbye! Total score: %i points." % tempScore
    
    
    
wordList = loadWords()
hand = {'h':1, 'i':1, 'c':1, 't':1, 'm':1, 'a':2}
n = 7

print playHand(hand, wordList, n)