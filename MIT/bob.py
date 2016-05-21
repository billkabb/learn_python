# My code
s = 'azcbobobegghakl'
bob = 'bob'
numBobs = 0
count1 = 0

for i in range(1, len(s)-1):
    count1 = s[i-1:i+2].count(bob)
    numBobs = numBobs+count1

print 'Number of times bob occurs is:', numBobs

#MIT code

numBobs = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Number of times bob occurs is:', numBobs
      
