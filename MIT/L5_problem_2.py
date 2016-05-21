def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    base = float(base)
    if exp ==1:
        return base
          
    elif exp != 0:
        return base * recurPower(base, exp-1) 
    else :
        return 1.0
    
       
print recurPower(2.23, 0)
