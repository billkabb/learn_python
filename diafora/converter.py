#print bin(100)#dekadiko se binary
#print int(0b101)#binary se dekadiko
#print oct(8)#octal se dekadiko
#print hex(10)#dkadiko se hex

class converter:
    def __init__(self):
        print "\n\n"
        print "\t'Converter' "
        print "\t __________ "
        print "\t|          |"
        print "\t|   Made   |"
        print "\t|    by    |"
        print "\t| billkabb |"
        print "\t|    **    |"
        print "\t|__________|\n\n"
        
    def BinaryToInteger(self):
    
        while True:
            try:
                print "Type binary numbers."
                print "Put '0b' in front of it."
                print "for examble binary of '1' , type '0b1' :"
                
                out = raw_input("\nPress 'm', to go to menu OR press 'enter' to continue : ")
                
                if(out=='m'):
                    print "\n\n"
                    self.menu()
                    
                binary = input("\nEnter a binary-number: ")
                integer=int(binary)
                
                print "\nThe integer number is:",integer,"\n\n"
                raw_input()
            except:
                print "\nSomething was wrong.\nTry again.\n\n"
                
                
                
    def IntegerToBinary(self):
    
        while True:
            try:
                print "Type integer numbers."
                
                out = raw_input("\nPress 'm', to go to menu OR press 'enter' to continue : ")
                
                if(out=='m'):
                    print "\n\n"
                    self.menu()
                        
                integer = input("\nEnter an integer-number: ")
                binary = bin(integer)
                
                str_bin=str(binary)
                str_bin=str_bin.replace("0b","")
                
                print "\nThe binary number is:",str_bin,"\n\n"
                raw_input()
                
            except:
                print "\nSomething was wrong.\nTry again.\n\n"
                
                
    def OctalToInteger(self):
    
        while True:
            try:
                print "Type octal numbers."
                print "Put '0' in front of it."
                print "for examble octal of '1' , type '01' :"
                
                out = raw_input("\nPress 'm', to go to menu OR press 'enter' to continue : ")
                
                if(out=='m'):
                    print "\n\n"
                    self.menu()
                             
                octal = input("\nEnter an octal-number: ")
                integer = int(octal)
                
                print "\nThe integer number is:",integer,"\n\n"
                raw_input()
            except:
                print "\nSomething was wrong.\nTry again.\n\n"
    
    
    def IntegerToOctal(self):
    
        while True:
            try:
                print "Type integer numbers."
                         
                out = raw_input("\nPress 'm', to go to menu OR press 'enter' to continue : ")
                
                if(out=='m'):
                    print "\n\n"
                    self.menu()
                        
                integer = input("\nEnter an integer-number: ")
                octal = oct(integer)
                
                list_oct = list(octal)
                list_oct[0] = ""
                
                print "\nThe octal-number is:",''.join(list_oct),"\n\n"
                raw_input()
            except:
                print "\nSomething was wrong.\nTry again.\n\n"
    
    
    def HexadecimalToInteger(self):
    
        while True:
            try:
                print "Type hexadecimal numbers."
                print "Put '0x' in front of it."
                print "for examble hexadecimal of '1' , type '0x1' :"
                
                out = raw_input("\nPress 'm', to go to menu OR press 'enter' to continue : ")
                
                if(out=='m'):
                    print "\n\n"
                    self.menu()
                        
                hexadecimal = input("\nEnter a hexadecimal-number: ")
                integer = int(hexadecimal)
                
                print "\nThe integer number is:",integer,"\n\n"
                raw_input()
            except:
                print "\nSomething was wrong.\nTry again.\n\n"
                
                
                
                
    def IntegerToHexadecimal(self):
        while True:
            try:
                print "Enter only integer number"
                
                out = raw_input("\nPress 'm', to go to menu OR press 'enter' to continue : ")
                
                if(out=='m'):
                    print "\n\n"
                    self.menu()
                        
                integer = input("\nEnter an integer-number:")
                hexadecimal=hex(integer)
                
                str_hex = str(hexadecimal)
                str_hex = str_hex.replace("0x","")
                
                print "\nThe hexadecimal number is:",str_hex,"\n\n"
                raw_input("Press 'Enter' to continue")
            except:
                print "\nSomething was wrong.\nTry again.\n\n"
                
                
                
    def menu(self):
        print "1) Convert Binary to Integer."
        print "2) Convert Integer to Binary."
        print "3) Convert Octal to Integer."
        print "4) Convert Integer to Octal."
        print "5) Convert Hexadecimal to Integer."
        print "6) Convert Integer to Hexadecimal."
        
        try:
            choice = input("\nChoose a number (1-6): ")
            
            if (choice == 1):
                print "\n\n"
                self.BinaryToInteger()
            elif (choice == 2):
                print "\n\n"
                self.IntegerToBinary()
            elif (choice == 3):
                print "\n\n"
                self.OctalToInteger()
            elif (choice == 4):
                print "\n\n"
                self.IntegerToOctal()
            elif (choice == 5):
                print "\n\n"
                self.HexadecimalToInteger()
            elif (choice == 6):
                print "\n\n"
                self.IntegerToHexadecimal()
            elif (choice == 7):
                quit()
                
            else:
                print "\nPlease make a valid choice."
                print "\n\n\n"
                self.menu()
        except:
         #   print "\nPlease make a valid choice."
          #  print "\n\n\n"
            #quit()
            #break
            self.menu()
                
                 
                 
cv=converter()
cv.menu() 
