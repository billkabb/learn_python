#Bisection 
#kovw synexeia sth mesh mexri na vrv to svsto 
#
#to programma einai etsi :
#
#1) sthn arxh orizw (hi – lo – kai guessed=False)
#2) meta xrhsimopoiw thn while pou trexei mexri to guessed na ginei True
#3) mesa sthn while sthn arxh orizw mia parametro guess = (hi + lo) / 2
#	diladh 100 + 0 / 2, 100 +50 / 2 klp
#	kai amesws meta zhtw apo ton user na mou pei an to kathe guess
#einai panw h katw apo ton arithmo pou exei skeftei user_inp = raw_input(“wtw”)
#
#4)  if user_inp == 'c':
#        # We got it right!
#        guessed = True
#
#5) elif user_inp == 'h':
#        # Guess was too high. So make the current guess the highest possible guess.
#        hi = guess
#
#6) elif user_inp == 'l':
#        # Guess was too low. So make the current guess the lowest possible guess.
#        lo = guess
#
#7)    else:
#        print("Sorry, I did not understand your input.")
#
#8) kathe for a pou o user pataei 'h' paei na pei pws o arithmos tou user
#	einai mikroteros apo thn mantepsia mou kai ara thetw 
#	kainourio hi ekei pou htan proigoumews to guess diladh hi+lo/2
#	klp klp kai csanarwtaw mexri na to vrw
#
#8) telos an vrethei o arithmos kai o user to epivevaivsei patwntas
#	'c' tote to guessed ginetai True 
#	to programa vgainei apo thn while kai
#9)ektypwnei 
#	print('Game over. Your secret number was: ' + str(guess))
#
#o kwdikas einai :

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

