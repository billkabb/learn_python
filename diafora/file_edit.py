import os

path=raw_input("Enter the path: ")
path+=".txt"

choose=input("1)Write.2)Read.3)Append.4)Delete: ")

if choose==1:
    py=open(path,"w")
    words=raw_input(">>>")
    py.write(words)
    py.close()
    
elif choose==2:
    py=open(path,"r")
    print "Enter number of bytes"
    bytes=input(">>>")
    print py.read(bytes)
    py.close()
    
elif choose==3:
    py=open(path,"a")
    words=raw_input(">>>")
    py.write(words)
    py.close()
    
elif choose==4:
    os.remove(path)
    
else:
    print "Wrong"




