from random import choice

#a=['hello','hi','bye']
#b=choice(a)
#print b                    # kodikas gia tyxaia epilogi

win=0
times=0
check=0
the_words=["dog","cat","dude","bill"]

word=choice(the_words)
length=len(word)
text="*" *length


class my_game:
    def show(self):
        print text
        
    def hangman(self):
        if (times==0):
            print " +---+"
            print " |   |"
            print "     |"
            print "     |"
            print "     |"
            print "     |"
        elif (times==1):
            print " +---+"
            print " |   |"
            print " O   |"
            print "     |"
            print "     |"
            print "     |"
        elif (times==2):
            print " +---+"
            print " |   |"
            print " O   |"
            print " |   |"
            print "     |"
            print "     |"
        elif (times==3):
            print " +---+"
            print " |   |"
            print " O   |"
            print " |-  |"
            print "     |"
            print "     |"
        elif (times==4):
            print " +---+"
            print " |   |"
            print " O   |"
            print "-|-  |"
            print "     |"
            print "     |"
        elif (times==5):
            print " +---+"
            print " |   |"
            print " O   |"
            print "-|-  |"
            print "  \  |"
            print "     |"
        elif (times==6):
            print " +---+"
            print " |   |"
            print " O   |"
            print "-|-  |"
            print "/ \  |"
            print "     |"
        elif (times==7):
            print "You lost :-("
            
            
my_obj = my_game()

print "Give your name:"
name = raw_input(">>>")


while (win==0):
    print "\nHere is the word :"
    my_obj.show()
    
    print "\n",name,"give a letter :"
    letter = raw_input(">>>")
    
    if (letter in word):
        for count in range(length):
            if (letter in word[count]):
                text = text[:count] + word[count] + text[count+1:]
    else:
        times+=1
        
    if ("*" not in text):
        win = 1
        my_obj.show()
        print "You won :-)"
        
    if (times == 7):
        win = 1
        my_obj.show()
        
    my_obj.hangman()
