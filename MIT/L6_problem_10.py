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

First, write a procedure, called howMany, which returns the sum of the number of values associated with a dictionary. For example:

>>> print howMany(animals)
6

"""
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
test={}
#print len(test.keys())
#a=animals.keys()
#print a[2]
#print 
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    a=aDict.keys()
    b=0
    if len(aDict)==0:
        return len(aDict)
    else:
        for i in range(len(aDict.keys())):
            #c=b+len(aDict[a[i]])
            b+=len(aDict[a[i]]) #a=len(animals('a'))
        
        #print c #return animals
        return b

print howMany(animals)

########
# MIT #
#######

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result

def howMany2(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

print howMany(animals)



