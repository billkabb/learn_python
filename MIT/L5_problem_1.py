def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp != 0:
        result=base
        for i in range(exp-1):
            result=result*base
        return result   
    else:
        return 1.000
print iterPower(9,3)
