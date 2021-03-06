from ps4a import *
import time
import random
#import sys
#from sys import exit

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
    #print listHand 
    #print len(tempList)
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
    #print "Words found: " , len(tempWordList)
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
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... 
    tempScore = 0
#   while calculateHandlen(hand):    
#        tempHand = hand.copy() 
#        #tempScore = 0
#        listHand = []
#        for i in tempHand:
#            if tempHand[i]> 0:
#                for j in range(tempHand[i]):
#                    listHand.append(i)
            #print listHand
        
    #print "Current Hand: %s" % ' '.join(hand)
    #word = raw_input('Enter word, or a "." to indicate that you are finished: ')
#    word=compChooseWord(hand, wordList, n)
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
        print
        print "Current Hand: %s" % ' '.join(listHand)
        word = compChooseWord(hand, wordList, n)
        
        if word == ".":
            break        
        
        elif not isValidWord(word, hand, wordList):
            print "Total score: %i points." % tempScore
            break
        elif isValidWord(word, hand, wordList):
            tempScore += getWordScore(word, n)
            print '"%s" earned %i points. Total: %i points\n' % (word , getWordScore(word, n) , tempScore)
            hand = updateHand(hand, word)
    
        print "Total score: %i points." % tempScore
    #return tempScore
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    hand = {}    
    while wordList:
        print
        userSel = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        print userSel
        if userSel not in ("r","n","e","."):
            print "Oops .. Invalid command."
            print
        if userSel == "n":
            print
            userSel1 = raw_input('Enter u to have yourself play, c to have the computer play: ')
            print
            if userSel1 not in ("c","u"):
                print "Invalid command."
                print
            
            if userSel1 == "u":
                #print "n" 
                hand = dealHand(n)
                #print hand
                playHand(hand, wordList, n)
                print
            if userSel1 == "c":
                hand = dealHand(n)
                compPlayHand(hand, wordList, n)
        if userSel == "r" :#and hand: 
            if hand != {}:
                print
                userSel2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if userSel2 not in ("c","u"):
                    print "Invalid command."
                    print
            
                if userSel2 == "u":
                #print "n" 
                #hand = dealHand(n)
                #print hand
                    playHand(hand, wordList, n)
                    print
                if userSel2 == "c":
                    #hand = dealHand(n)
                    compPlayHand(hand, wordList, n)

#                playHand(hand, wordList, n)
#                print #"r"
            else:
                print "You have not played a hand yet. Please play a new hand first!"
                print    
            
#        if userSel == "r" and not hand:    
#            print "You have not played a hand yet. Please play a new hand first!"
        if userSel == "e":
            raise SystemExit
            #sys.exit()


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


