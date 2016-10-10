def func(n):             #1+2+3.... athroisma tou 3 = n(n+1)/2
    
    p=n*(n+1)/2
    return p
    
print func(4)


####### Or ( paradeigma gia synasrtisi mesa sth synartisi)

def func(n):
    p=0
    for i in range(1,n+1):
        p=p+i
    return p
    
    
print func(4)

########or me anadromi

def func(n):
    p=0
    if n==1:
        return 1

    p=n+func(n-1)
    return p
    
print func(4)
