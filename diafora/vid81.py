def func(n):             #1*2*3.... paragwntikos arithmos tou 3
    p=1
    for i in range(1,n+1):
        p=p*i
        
    return p
    
print func(4)


####### Or ( paradeigma gia synasrtisi mesa sth synartisi)

def func(n):
    if n == 1:
        return 1
    p=n*func(n-1)
    
    return p
    
    
print func(4)
