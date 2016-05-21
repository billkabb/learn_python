def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    if a == 0 or b==0:
		print 'No common divider found'
        #return 
    elif a != 0 :#and a < b: 
		testValue = min(a, b)
		for i in range(testValue,0,-1):
			#print i
			if b%(i)==a%(i) and b%(i)==0 :
				return i
				#print i#,b%(i),a%(i)
			
			##return base * recurPowerNew(base, exp-1)
    #elif exp > 0 and exp % 2 == 0:
        #return recurPowerNew(base*base, exp/2)
    #else:
        #return base * recurPowerNew(base, exp+1)
        
print gcdIter(9, 13)

#MIT solution

def gcdIter1(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue

print gcdIter1(9, 27)    
