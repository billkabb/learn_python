# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:02:32 2016

@author: billkabb
"""

"""
Python is an MIT student who loves fruits. He carries different types of fruits (represented by capital letters) daily from his house to the MIT campus to eat on the way. But the way he eats fruits is unique. After each fruit he eats (except the last one which he eats just on reaching the campus), he takes a 30 second break in which he buys 1 fruit of each type other than the one he just had. Cobra, his close friend, one day decided to keep a check on Python. He followed him on his way to MIT campus and noted down the type of fruit he ate in the form of a string pattern (Eg.: 'AABBBBCA'). Can you help Cobra determine the maximum quantity out of the different types of fruits that is present with Python when he has reached the campus?

Write a function nfruits that takes two arguments:

    A non-empty dictionary containing type of fruit and its quantity initially with Python when he leaves home (length < 10)
    A string pattern of the fruits eaten by Python on his journey as observed by Cobra.

This function should return the maximum quantity out of the different types of fruits that is available with Python when he has reached the campus.

For example, if the initial quantities are {'A': 1, 'B': 2, 'C': 3} and the string pattern is 'AC' then

    'A' is consumed, updated values are {'A': 0, 'B': 2, 'C': 3}
    Python buys 'B' and 'C', updated values are {'A': 0, 'B': 3, 'C': 4}
    'C' is consumed, updated values are {'A': 0, 'B': 3, 'C': 3}

Now Python has reached the campus. So the function will return 3 that is maximum of the quantities of the three fruits.
vazw +1 se ola arxika kai kathe fora afairw 2 apo to trexon kai mono afairw ena apo to teleytaio
"""
def nfruits(x, y):
    #print x , y
    b=x
    #print b
    for i in b:
        b[i]+=(len(y)-1)
        #print b[i], len(y)-1 ,b
    for i in y[:-1]:
        b[i]-=2
        #print i, b[i]
        #if i in 
    for i in y[-1]:
        b[i]-=1
    return max(b.values())
    
#x = {'A': 1, 'B': 2, 'C': 3}
#y = 'AC'
x = {'U': 6}
y = 'UUUUU'

print nfruits(x, y)