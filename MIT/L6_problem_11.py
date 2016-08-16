# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 01:31:40 2016

@author: billkabb
"""

"""
Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

Example usage:

>>> biggest(animals)
'd'

If there are no values in the dictionary, biggest should return None. 
"""
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals1 = {'a': [3, 18, 18, 10, 2, 8, 15, 15, 20, 17], 'c': [0, 19], 'b': [], 'e': [9, 10, 10], 'd': [10, 9, 15, 5, 17, 19, 19, 0, 12]}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

#print max(aDict.values())
#a=animals.keys()
#print a[2]
#print 
def biggest(aDict):
    #print aDict.items()
    
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    
    a=[]    
    b=[]
    if len(aDict) > 0:
        for key in aDict.keys():
            
            a.append(len(aDict[key]))
            b.append(key)
        
        return b[a.index(max(a))] 
        

print biggest(animals1)

########
# MIT #
#######
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        #print aDict[key]
        if len(aDict[key]) >= biggestValue:
            #print 
            result = key
            biggestValue = len(aDict[key])
    return result
print biggest(animals1)