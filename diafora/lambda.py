#dhmiourgei antikeimena synartisewn vid76
def func(n):
    return lambda a:a*n
    
obj=func(3)    #diladi opou n == 3
print obj(2)   #diladi opou a == 2 diladh sto telos mas dinei 2*3=6

a=input(">>>") #mporei na einai arithmos h kai lecsi "test"

if (a==2):
    print obj(2)
elif (a==3):
    print obj(3)
    
else:
    print obj(a)
    
###########################
a,b=1,2
#gia na antistrepsw times
a,b=b,a

