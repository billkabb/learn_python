from random import randint


def fill_board(fake_board):
  for x in range(0,5):
    fake_board.append(["O"] * 5)


def print_board(fake_board):
   for var in fake_board:
        print " ".join(var)


def random_row(fake_board):
    return randint(1, len(fake_board))
    

def random_col(fake_board):
    return randint(1, len(fake_board))





board=[]
i=5
win=0




fill_board(board)
check=len(board)-1



ship_row=random_row(board) 
ship_col=random_col(board)
ship_row-=1
ship_col-=1




if(ship_row==4 and ship_col==4):
    luck=randint(1,2)

    if(luck==1):
        ship_row1=ship_row
        ship_col1=ship_col-1
   
    elif(luck==2):
        ship_row1=ship_row-1
        ship_col1=ship_col

        
elif(ship_row==4):
    ship_row1=ship_row
    ship_col1=ship_col+1


elif(ship_col==4):
    ship_row1=ship_row+1
    ship_col1=ship_col 


else:
    luck=randint(1,2)

    if(luck==1):
        ship_row1=ship_row
        ship_col1=ship_col+1
   
    elif(luck==2):
        ship_row1=ship_row+1
        ship_col1=ship_col




        
print_board(board)




while(i>0):    
    guess_row=input("\nGuess Row:")
    guess_col=input("Guess Col:")

    guess_row-=1
    guess_col-=1


        
    if(guess_row<0 or guess_row>check or guess_col<0 or guess_col>check):
        print "\n\n\nThis option is invalid."
        print "You have",i,"tries\n"
        print_board(board)

        

    elif(board[guess_row][guess_col]=="X" or board[guess_row][guess_col]=="N"):
        print "\n\n\nYou guessed that one already."
        print "You have",i,"tries\n"
        print_board(board)
   


    elif((guess_row==ship_row and guess_col==ship_col) or (guess_row==ship_row1 and guess_col==ship_col1)):
        board[guess_row][guess_col]="N"
        win+=1
        print_board(board)

    
    else:
        board[guess_row][guess_col]="X"
        i-=1
        print "\n\n\nYou missed my battleship!"
        print "You have",i,"tries\n"
        print_board(board)


    if(win==2):
        print "\n\n\n"
        print_board(board)
        print "\n\nCongratulation!!!\nYou won!!!"
        break
        

            
if(i==0):
    print "\n\n\n"
    board[ship_row][ship_col]="A"
    board[ship_row1][ship_col1]="A"
    print_board(board)
    print "\n\nGame Over!\n"
