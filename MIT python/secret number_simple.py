print("Please think of a number between 0 and 1000!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 1000
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)/2
    print("Is your secret number dude ?" + str(guess)+ "?")
    user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))

##is_valid=0
##
##while not is_valid:
##    try:
##        num = int(raw_input("Please think of a number between 0 and 100!"))
##        if num in range(0,100):
##            is_valid=1
##        else:
##            print ("Number '%s' out of range , Try again" % num)
##    except ValueError, e :
##        print ("'%s' is not a valid answer " % e.args[0].split(": ")[1])
#num = int(num)
#print type(num),
#print num
##print "Please think of a number between 0 and 100!"
##ans = 'no'
##num1 = 50
##num2 = 100
##num3 =0
##trys = 0
##
##    while ans == 'no':
##        #num1 = num1/2
##        ans = raw_input("is your secret number '%s' ?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.\nEnter 'c' to indicate I guessed correctly." % int(num1))
##
##        if ans == str('l'):
##
##            num1 = num1+((num2-num1)/2.0)
##            ans = 'no'
##            trys+=1
##            print 'num1 is:' , num1
##            print 'num2 is:' , num2
##
##    elif ans==str('h') :
##
##        num3 = num1
##        num1 = num1-((num2-num1)/2.0)
##        num2=num3
##        ans = 'no'
##        trys+=1
##        print 'num1 is:' , num1
##        print 'num2 is:' , num2
##
##    elif ans == str('c') :
##        print 'your number is : "%s"' %int(num1)
##        print 'number found after "%s" guwsses' %trys
##
##    elif ans != ('h' or 'l' or 'c'):
##        print 'this is not a valid answer , please enter ("h","l" or "c")'
##        ans = 'no'
##
##

##if num in range(0,99):
##    print num
##else:
##    print "This number is out of range"
