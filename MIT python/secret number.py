
is_valid=0

while not is_valid:
    try:
        num = int(raw_input("Please think of a number between 0 and 100!"))
        if num in range(0,100):        
            is_valid=1
        else:
            print ("Number '%s' out of range , Try again" % num)
    except ValueError, e :
        print ("'%s' is not a valid answer " % e.args[0].split(": ")[1])
#num = int(num)
#print type(num),
#print num

ans = 'no'
num1 = 50
num2 = 100
num3 =0
trys = 0

while ans == 'no':
    #num1 = num1/2
    ans = raw_input("Is your secret number '%s' ?" % int(num1))
    
    if ans == str('l'):
        
        num1 = num1+((num2-num1)/2.0)
        ans = 'no'
        trys+=1
        print 'num1 is:' , num1
        print 'num2 is:' , num2
        
    elif ans==str('h') :
        
        num3 = num1
        num1 = num1-((num2-num1)/2.0)
        num2=num3
        ans = 'no'
        trys+=1
        print 'num1 is:' , num1
        print 'num2 is:' , num2

    elif ans == str('c') :
        print 'your number is : "%s"' %int(num1)
        print 'number found after "%s" guwsses' %trys

    elif ans != ('h' or 'l' or 'c'):
        print 'this is not a valid answer , please enter ("h","l" or "c")'
        ans = 'no'



##if num in range(0,99):
##    print num
##else:
##    print "This number is out of range"
