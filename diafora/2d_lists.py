board=[]

for i in range(4):
    board.append([])
    #print board[i]
    for x in range(4):
        board[i].append(x)
        
        
#print board
for var in range(4):
    print board[var]
    
####### OR
for var in board:
    print var
    
### ALLIWS gia 2d pinaka grafw

board=[]

for i in range(4):
    board.append(['s']*4)

for var in board:
    print var 
### or
for var in range(4):
    print " ".join(board[var])
    
### or
for var in range(4):
    for var1 in range(3):
        print board[var][var1]
