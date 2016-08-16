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
def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

gen = genFib()
#call gen.next() from command line
''' gia paradeigma exw to ariyhmo 13 , arxizontas apo to 2
13 % 2 = 1    1
13 % 3 = 1    2
13 % 5 = 3    3
13 % 7 = 6    4
13 % 9 = 4    5
13 % 11 = 2   6
ara einai prime otan kanenas monos apo tous proigoumenos kai megalhteros tou 1
 den ton diairei akrivws
'''
#def genPrimes():
#    n = 3
#    l = [2]
#    next = 2
#    while True:
#        temp = []
#        
#        if n %2 == 1:
#            l.append(n)
#            for k in l:
#                if n%k != 0:
#                    temp.append(k)
#            if len(l) == len(temp)+1:
#                yield next                
#                next = n
#                
#        n+=1
#
#gen = genPrimes()
#gen