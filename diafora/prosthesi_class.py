class mine():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,other):
        return mine(self.a+other.a , self.b+other.b) # h pracsh mporei na einai kai - , / or *
        
    def __str__(self):
        return 'Results: %d , %d' %(self.a,self.b)
        
        
m=mine(2,3)
m1=mine(4,5)
m2=mine(6,7)

print m+m1+m2


#overload operators
#-------------------#

# gia afairesi xrisimopoiw sub diladi def __sub__(self,other):
# kai kalw print m-m1-m2
#gia pollaplasiasmo xrisimopoiw mul , diairesi div

#allos tropos
#  def __add__(self,other):
#        a=self.a*other.a
#        b=self.b*other.b
#        return mine(a,b)

