# video80

import sys
count=0

def wordlist(fake_buffer,fake_compination_length,fake_characters,fake_characters_length,fake_count):
    file=open("wordlist.txt","w")
    
    global count
    index_list=[]
    
    for i in range(0,fake_compination_length):
        index_list.append(0)
        
    pos=fake_compination_length-1
    
    while(True):
        if(index_list[pos] == fake_characters_length):
            while(index_list[pos] == fake_characters_length):
                pos-=1
                index_list[pos]+=1
                if(pos < 0):
                    return
            for i in range(fake_compination_length-1,pos,-1):
                index_list[i]=0
            pos=fake_compination_length-1
            
        for i in range(0,fake_compination_length):
            fake_buffer.append(fake_characters[index_list[i]])
            sys.stdout.write(fake_buffer[i])
            file.write(fake_buffer[i])
            
        file.write("\n")
        del fake_buffer[0:len(fake_buffer)]
        
        print ""
        index_list[pos]+=1
        
        count+=1
        
    file.close()
    
    
buffer=[]
characters=[]
char=""

while(char!="exit"):
    char=raw_input("Enter char(s): ")
    characters.append(char)
    
characters.pop()
chars_length=len(characters)

compination_length=input("\nEnter the length: ")

print ""

wordlist(buffer,compination_length,characters,chars_length,count)

print "\nPossible compinations: "+str(count)
                


