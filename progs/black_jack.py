from random import randint
import time

player=1

point_1 = 0
point_2 = 0

run_1 = True
run_2 = True


def showcard(num):
	print ".------."
	print "|",num,".--|"
	print "| :/\: |"
	print "| :\/: |"
	print "| '-",num,"|"
	print "`------'\n"



def check_player():
    global player
    global run_1
    global run_2
    
    if(run_1==True and run_2==True):      
        if(player%2==0):
            player=2

        else:
            player=1
            

    else:
        if(run_1==False):
            player=2

        elif(run_2==False):
            player=1




	
print """
.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'
"""

choice = input("1)Player1 vs Player2\n2)Player1 vs Computer\n\nChoice ==> ")


if(choice==1):
  print "\n"   
  while(True):
        check_player()
        
        print "\n\nPlayer",player,"want a card? (y/n)"
        input=raw_input(":")

        if(player==1 and run_1==True):
            if(input=="y"):
                add1=randint(1,10)
                point_1=add1+point_1
                showcard(add1)
                print "All your points are",point_1,"\n\n"

            elif(input=="n"):
                run_1=False
                
                
               

        elif(player==2 and run_2==True):
            if(input == "y"):
                add2 = randint(1,10)
                point_2 = add2 + point_2
                showcard(add2)
                print "All your points are",point_2,"\n\n"
			
            elif(input == "n"):
                run_2 = False





        if(run_1 == False and run_2 == False):
            if(point_1 == point_2):
                print "\nTie!"
                break
		    
            elif(point_1 > point_2):
                print "\nPlayer 1 wins ! "
                break
		    
            elif(point_1 < point_2):
                print "\nPlayer 2 wins ! "
                break	





	
        if(point_1 > 21):
            print "Player 2 wins ! "
            break


        elif(point_2 > 21):
            print "player 1 wins ! "
            break


	    
        player+=1
        
	





elif(choice==2):
  print "\n"   
  while(True):
        check_player()

        if(player==1):
          print "\n\nPlayer",player,"want a card? (y/n)"
          input=raw_input(":")

        elif(player==2):
            print "\n\nComputer is thinking..."
            time.sleep(3)

            
        if(player==1 and run_1==True):
            if(input=="y"):
                add1=randint(1,10)
                point_1=add1+point_1
                showcard(add1)
                print "All your points are",point_1,"\n\n"

            elif(input=="n"):
                run_1=False
                
                
               
        elif(player==2 and run_2==True):
            if(point_2<15):
                add2 = randint(1,10)
                point_2 = add2 + point_2
                showcard(add2)
                print "Computer points are",point_2,"\n\n"
			
            else:
                run_2 = False





        if(run_1 == False and run_2 == False):
            if(point_1 == point_2):
                print "\nTie!"
                break
		    
            elif(point_1 > point_2):
                print "\nPlayer 1 wins ! "
                break
		    
            elif(point_1 < point_2):
                print "\nComputer wins ! "
                break	





	
        if(point_1 > 21):
            print "Computer wins ! "
            break


        elif(point_2 > 21):
            print "player 1 wins ! "
            break


	    
        player+=1    





else:
    print "\nWrong Choice."
