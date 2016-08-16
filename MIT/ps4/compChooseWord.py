# -*- coding: utf-8 -*-
from ps4a import *
import random
import time
n = 7 
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
#import ps4a


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)

    # Create a new variable to store the best word seen so far (initially None)  

    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly

    #fernv oles tis lecsies pou exoun extw ena gramma apo to hand
    #vgazw ta duplicates
    #twra exw mia lista me pithanes lecseis 
    #ftiaxnw ena dict me key thn lecsh kai value to score ths lecshs 
    #sortarv ana value
    # return the best word you found.
    maxScore = 0
    bestWord = None
    tempWordList = []
    tempDict = {}
    tempHand = hand.copy() 
    tempList = wordList[:]
    #tempScore = 0
    listHand = []
    #empty = []
    tempMax = []
    for i in tempHand:
        
        if tempHand[i]> 0:
            for j in range(tempHand[i]):
                listHand.append(i)    
    print listHand 
    print len(tempList)
    # twra exw thn listHand pou einai mia lista me ta grammata tou hand
    #        
    for i in tempList: # gia kathe lecsh ths listas
        empty = []
        newList = listHand[:] #a
        word = i #b
        #print temp , "123"
        for j in i: # gia kathe gramma ths lechs
            if j in newList:
                newList.remove(j)
                empty.append(j)
        if len(i) == len(empty):    
            #print empty , i 
            tempWordList.append(i) # to i vazei string , to empty lista
            #print len(tempWordList) 
            #raw_input("Press Enter to continue...")
 ###############na grapsw try except gia an den brei lecsh   
    print "Words found: " , len(tempWordList)
    for i in tempWordList:
        tempSum = 0
        for j in i:
            tempSum+=(SCRABBLE_LETTER_VALUES[j]*len(i))
        if len(i)==n:
            tempSum+=50
        #print i , tempSum
        tempDict[i] = tempSum
        #print tempDict
        #raw_input("Press Enter to continue...")
    
    #print max(tempDict.values()) ,n
    for i in tempDict.keys():
        if tempDict[i] == max(tempDict.values()):
            #print tempDict[i]
            tempMax.append(i)
            break
    #print tempMax,random.choice(tempMax)
    #print "MaxScore and Word are: " ,max(tempDict.values()), i
    try:
        bestWord = random.choice(tempMax)
        return bestWord
    except:
        return None
    #return i

wordList = loadWords()        
hand = dealHand(n).copy()
#hand = {'c': 1, 'r': 1, 'l': 1}
print hand
#print sorted(SCRABBLE_LETTER_VALUES , key=SCRABBLE_LETTER_VALUES.get, reverse=True)

print compChooseWord(hand, wordList, n)