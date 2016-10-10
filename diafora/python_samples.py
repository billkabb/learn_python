#!/usr/bin/env python
##########
#example factorial 1*2*3*4
#def factorial(x):
#    
#    if x == 0 :
#        return 1
#    else:
#        return x * factorial(x - 1)
#        
#            
#print factorial(4)

##def is_prime(num):
##
##    if num > 1:
##       # check for factors
##       for i in range(2,num-1):
##           if (num % i) == 0:
##               print(num,"is not a prime number")
##               print(i,"times",num//i,"is",num)
##               return False
##               break
##       else: # edw ekana indent lathos
##           print(num,"is a prime number")
##           return True
##           
##    # if input number is less than
##    # or equal to 1, it is not prime
##    else:
##       print(num,"is not a prime number")  
##       return False
##is_prime(0)

##def reverse(text):
##    list = []
##    lista = []
##    listc = []
##    for c in text:  #vazw ta grammata ths lecshs se lista
##        list.append(c)     
##        x = int(len(list))  #posa grammata exei h lecsh
##        lista.append(-x)    #ta vazw se mia lista arnitika
##    for d in lista:     
##        listc.append(list[d])  #vazwto -1,-2 klp position se listac   
##    print ''.join(listc)    # kanw ', '.join gia na vgoun swsta
##    return ''.join(listc)
##      
##reverse("Python!")
