# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:26:13 2016

@author: billkabb
"""
'''
Write a generator, genPrimes, that returns the sequence of prime numbers 
on successive calls to its next() method: 2, 3, 5, 7, 11, ...
2 3 5 7 11 13
'''
def genPrimes():
    n = 3
    l = [2]
    next = 2
    while True:
        temp = []
        
        if n %2 == 1:
            l.append(n)
            for k in l:
                if n%k != 0:
                    temp.append(k)
            if len(l) == len(temp)+1:
                yield next                
                next = n
                
        n+=1
        
gen = genPrimes()
#gen
# kai trexw gen.next() apo command