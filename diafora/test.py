##a = input()
##for i in a:
##    print(i)

##x=[]
##for i in range(0,5):
##    x.append(input("vale: "))
##
##print(x)

##a = "I like python Python very much"
##list1 = a.split()
##counter = 0
##for i in list1:
##    if i.lower() == "python" :
##        counter+=1
##
##print(counter)

##def method1(n):
##    print("you clled metho1 with argument ",n)
##
##method1("maria")

##def method1(n):
##    n=n+1
##    return n
##
###method1(10)
##var1 = method1(10)
##print(var1) 


def check(n):
    apot="Mono"
    if n%2==0:
        apot="Zygo"
    return apot

arithmos = int(input("Arithmos: "))
while arithmos == 0 or arithmos < 0:
    arithmos = int(input("vale pali arithmo"))
apotelesma = check(arithmos)
print(apotelesma)
