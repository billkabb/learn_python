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
def genPrimes(x):
   
    L=[2]
    L1={}
    i = 2
    while i < x:
        #print i
        
        if i%2 ==1:
            L.append(i)
            #print L
            for k in L:
                #print k, i
                if i%k!=0:
                    L1[i]=L1.get(i, 0) + 1
                     
                
        i+=1
    
    listVal = L1.values()
    listKey = L1.keys()
    listPrime=[]
    for i in range(len(L1)):
        #print  i+1 , L1.values() ,listVal[i] , listKey[i]
        
        if i+1 == listVal[i]:
            
            listPrime.append(listKey[i])
            
#            next = listKey[i]
#            yield next
            #yield listKey[i]
            
#    yield listKey[i]
    print listPrime
    #return listPrime
            
        
    
        
#x = 10
gen = genPrimes(100)
print gen
#print 13 % 2
#print 13 % 3
#print 13 % 5
#print 13 % 7
#print 13 % 9
#print 13 % 11
#print gen.next()
        
#def fibonacci(n):
#    """Fibonacci numbers generator, first n"""
#    a, b, counter = 0, 1, 0
#    while True:
#        if (counter > n): return
#        yield a
#        a, b = b, a + b
#        counter += 1
#f = fibonacci(5)
#for x in genPrimes(30):
#    print x.next()
#print
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

