class mine:
    def __init__(self,name):
        self.name=name
        
    def __cmp__(self,other):
        if (self.name < other.name):
            return -1
        elif (self.name > other.name):
            return 1
        else:
            return 0
        
        
        
m=mine(2)
m1=mine(4)

if (m>m1):
    print "first is bigger"
elif (m<m1):
    print "first is smaller"
else:
    print "are equal"
