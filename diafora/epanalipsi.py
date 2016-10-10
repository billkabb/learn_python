#listes
a=[1,2,3]

print a
#or
for b in a:
    print b
#or
for b in range(len(a)):
    print b
    #or
    print a[b]
    
#diagrafi apo lista
del a[1]
    print a
#
print len(a)
print min(a)
print max(a)
# sygkrisi
a=[1]
b=[2]

print cmp(a,b)
##### to global kanei mia var global
global x
#tuple
a=(1,2,3)
print list(a) #metatrepei to tupple se lista
#prosthetw sth lista
a=[1,2,3]
a.append(100)
#metra poses fores yparxei to 2 sth lista
print a.count(2)
#vazei mia lista sthn allh
a=[1,2,3,4]
b=["hello",5]
a.extend(b)
print a
# mas deixnei se poia thesi einai to "hello"
a=["hello",2,"world",100]
print a.index("hello")
#vazei stoixeio se sygkekrimenh thesi(vazei to 3 sth thesi 2)
a=["hello",2,"world",100]
a.insert(2,3)
#or
a.insert(1,"back")
#h pop epistrefei h ektypvne kai meta diagrafei ena stoixeio ths listas
a=["hello",2,"world",100]
print a.pop()#to teleytaio stoixeio
#or
a.pop(2)#th thesi 2 ths listas
print a
#diagrafei me to remove
a.remove("hello")
#to reverse ta vazei anapoda
a.reverse()
#to sort tacsinomei th lista
a.sort()
##################################tuples###################a=(
a=("hello",2,"world",100)

print a
# to cmp sygkrinei dyo tuples (1,0,-1) thesh pros thesi
a=(100)
b=(101)
print cmp(a,b)

#episis len(a) , max(a) , min(a) opws stis listes
# episis me tuple(a) kanw thn lista tuple kai me list(a) to tuple lista.
a=[1,2,3]
print tuple(a)
#####################################################kanw del kati apo th lista
a=["hepic","george","bill"]
print a
del a[0]
#######to clear adeiazei to dictionary
dict={"hepic":16,"george":12,"bill":5}
print a
dict.clear()
#or diagrafei olo to dictionary
del dict
#or diagrafei mia kataxwrish
del dict["bill"]
############ sygkrinei dyo dictionaries
dict={"hepic":19}
dict1={"bill":20}
a=cmp(dict,dict1)
print a
####
a={"hepic":19}
print type(a)  ### tha dwsei dict epeidi einai dictionary
####
print len(dict)
### to kanw string gia na to diaxeiristw diaforetika
dict1={"hepic":19}
a=str(dict1)
print a[2] #twra epeidi to vlepei san string mporw na ektypwsw to 2 stoixeio diladi to h
print a[1:7]
##########dictionaries methods
dict1={"bill":1}
dict2=dict1.copy() ## kanei copy 
#
seq=("hepic","bill")
dict=dict.fromkeys(seq) ### kanei ena tuple dictionary
print dict
dict=dict.fromkeys(seq,"value")# dinei timh.
#
seq=["hepic","bill"]
dict=dict.fromkeys(seq)### kanei th lista dictionary
#
dict={"hepic":16,"george":12,"bill":5}
print dict.get("hepic") #mas leei thn timh tou hepic diladi 16
print dict.get("hepic","Error not found")#ama den yparxei petaei error
#
print dict.has_key("hepic")#an yparxei petaei true an oxi false
#
dict={"hepic":16,"george":12,"bill":5}
list=dict.items()
print list[1]#dinei tis times tou dictionary san lista
#
print dict.keys()#petaei mono ta keys
print dict.values()#petaei mono ta values
#
dict={"name":"hepic","age":16,"sex":"male"}
dict1={"school":"maths","work":"programming"}

dict.update(dict1)###vazei olo to dict1 sto dict
print dict
###
a=5
b=2
#mporw omws na pw kai :
a,b=5,2
#gia na kanw antistrofh
a,b=5,2
temp=0
temp=a
a=b
b=temp
print a,b
# or
a,b=5,2
a,b=b,a
print a,b
