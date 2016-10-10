encrypted_alphabet=[]
encrypted_text=[]

def rotate(num):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    length_alphabet=len(alphabet)
    
    for i in range(len(alphabet)):
        pos=num+i
        
        if pos >= 26:
            pos=(num+i)-length_alphabet
            
        encrypted_alphabet.append(alphabet[pos])
    print encrypted_alphabet
        
def subcrypto(text):
    global encrypted_text
    
    alphabet="abcdefghijklmnopqrstuvwxyz"
    text=text.lower()
    
    for ch in text:
        idx=alphabet.find(ch)
        
        if idx!=-1:
            encrypted_text.append(encrypted_alphabet[idx])
            
        else:
            encrypted_text.append(" ")
            
    encrypted_text=''.join(encrypted_text)
    
fw=open("text","w")
text_w=raw_input("write something: ")
fw.write(text_w)
fw.close()

fr=open("text","r")
text_r=fr.read()
fr.close()

number=input("enter number (0-25): ")

rotate(number)
subcrypto(text_r)

fw=open("math3111 crypted text.txt","w")
fw.write("crypted text by math3111\n\n"+encrypted_text+"\nEnd of crypted text.")
fw.close()
