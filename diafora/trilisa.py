array=["0","1","2","3","4","5","6","7","8","9"]

def board():
    print "|"+array[1]+"|"+array[2]+"|"+array[3]+"|"
    print "-------"
    print "|"+array[4]+"|"+array[5]+"|"+array[6]+"|"
    print "-------"
    print "|"+array[7]+"|"+array[8]+"|"+array[9]+"|"
    
def win():
    if array[1] == array[2] and array[2] == array[3]:
        return 1
    elif array[4] == array[5] and array[5] == array[6]:
        return 1
    elif array[7] == array[8] and array[8] == array[9]:
        return 1
    elif array[1] == array[4] and array[4] == array[7]:
        return 1
    elif array[2] == array[5] and array[5] == array[8]:
        return 1
    elif array[3] == array[6] and array[6] == array[9]:
        return 1
    elif array[1] == array[5] and array[5] == array[9]:
        return 1
    elif array[3] == array[5] and array[5] == array[7]:
        return 1
    elif array[1] != "1" and array[2] != "2" and array[3] != "3" and array[4] != "4" and array[5] != "5" and array[6] != "6" and array[7] != "7" and array[8] != "8" and array[9] != "9":
        return 0
        
    else:
        return -1
        
def reset():
    array[1] = "1"
    array[2] = "2"
    array[3] = "3"
    array[4] = "4"
    array[5] = "5"
    array[6] = "6"
    array[7] = "7"
    array[8] = "8"
    array[9] = "9"    
    
playagain = "y"
while playagain == "y":
    player = 1
    i = win()
    while i == -1:
        print "\n"
        
        board()
        
        if player%2 != 0:
            player = 1
        else:
            player = 2
        if player == 1 :
            mark = 'X'
        else:
            mark = 'O'
        print "Player",player
        
        choice = input("play:")
        
        if choice == 1 and array[1] == '1':
            array[1] = mark
        elif choice == 2 and array[2] == '2':
            array[2] = mark
        elif choice == 3 and array[3] == '3':
            array[3] = mark
        elif choice == 4 and array[4] == '4':
            array[4] = mark
        elif choice == 5 and array[5] == '5':
            array[5] = mark
        elif choice == 6 and array[6] == '6':
            array[6] = mark
        elif choice == 7 and array[7] == '7':
            array[7] = mark
        elif choice == 8 and array[8] == '8':
            array[8] = mark
        elif choice == 9 and array[9] == '9':
            array[9] = mark
        else:
            print "\nINVALID MOVE \n"
            player-=1
            
        i=win()
        player=player+1
        
        
    board()
    if i==1:
        player-=1
        print "Player",player,"is the winner"
    if i==0:
        print "Game draw"
       
    playagain = raw_input("\nWanna play again (y/n) ? : ")
    if playagain=="y":
        
        print "\nYou choose to play again\n"
    elif playagain == "n":
        print "\n---Bye !!!---\n"
    else:
        print "\nPlease press 'y' or 'n'\n"
        
    print "*****"*40
    
    reset()
        
         
