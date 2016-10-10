class mine:
    def func(self):
        print "hello"
        
    def func1(self):
        self.func()     ############gia na doulepsei kalw mesw ths self thn func 
        print "hello guys"
        
m=mine()
m.func1()
###########################
import time

time.sleep(1)
print "Computer is thinking.."
time.sleep(3)
print "Computer is...."
