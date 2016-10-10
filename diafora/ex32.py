the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges','pears', 'apricocts']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this kind of for loop goes through list
for number in the_count:
    print 'This is count %d ' % number
    
#same as above
for fruit in fruits:
    print 'A fruit of type: %s' % fruit
    
# Also with mixed lists
# we use %r since we dont know whst is in it
for i in change:
    print 'I got %r' % i
    
#we can built lists starting wit an empty one
elements = []

#then use the range function to do the 0,5 counts
for i in range(0, 6):
    print 'adding %d to the list.' % i
    elements.append(i)
    
# now we can print them out too
for i in elements:
    print 'Elements was: %d' % i 
