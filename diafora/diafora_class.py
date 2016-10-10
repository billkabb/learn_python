class mine:
    __var=0                 # to __ kanoun thn var idiotiki kai den mporoume na thn kalesoume 
                            # ektos ths class . diladi me 'print mine.var'
    def add_print(self):
        self.__var+=1
        print self.__var
        
m=mine()

m.add_print()
m.add_print()
