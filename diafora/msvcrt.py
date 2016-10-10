# windows only

import msvcrt


while(1):
    char=msvcrt.getch()
    if (char==ord("a")):  #chr(97) einai to key "a"
        print "hey"       #diladi to chr() thelei ton arithmo enos char enw to ord() thelei to character
    else:
        print char
