s = 'qwertyeeoujisooo'
count = 0
count1=0
for letter in 'aeiou':
    #count=count+count1
    count1 = s.count(letter) #+ s.count('y')
    count=count+count1
print "Number of vowels:" + str(count)
    
    
##total = 0
##for c in s:
##    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
##        total += 1
##print "Number of vowels: " + str(total)
##
##ALTERNATE SOLUTION
##        
num = 0
for letter in s:
  if letter in "aeiou":
    num+=1
print "Number of vowels:" + str(num)
      
      
