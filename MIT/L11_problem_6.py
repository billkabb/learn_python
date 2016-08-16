# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:26:13 2016

@author: billkabb
"""
'''
In your Queue class, you will need three methods:

    __init__: initialize your Queue (think: how will you store the queue's elements? You'll need to initialize an appropriate object attribute in this method)
    insert: inserts one element in your Queue
    remove: removes (or 'pops') one element from your Queue and returns it. If the queue is empty, raises a ValueError.

'''

#
class Queue(object):
    
    def __init__(self):
        self.list = []
        
    
    def insert(self, e):
        
        
        self.list.insert(0, e)
        
        
    def remove(self):
        try:
            return self.list.pop()
             
        except:
            raise ValueError()
    def __str__(self):
        
        return '{' + ','.join([str(e) for e in self.list]) + '}' 

#MIT
#class Queue(object):
#
#    def __init__(self):
#        "Initializes 1 attribute: a list to keep track of the queue's elements"
#        self.qlist = []
#
#    def insert(self, element):
#        "Adds an element to the attribute list using append"
#        self.qlist.append(element)
#
#    def remove(self):
#        "Removes an element from the attribute list"
#        # Check if the list is empty; if so then raise a ValueError
#        if self.qlist == []:
#            raise ValueError()
#        else:
#            # Otherwise we want to remove the first element from the list
#            # and return that to the user.
#            element = self.qlist[0]
#            self.qlist.remove(element)
#            return element
#            # Could also do this in 1 line:
#            # return self.qlist.pop(0)
#    def __str__(self):
#        
#        return '{' + ','.join([str(e) for e in self.list]) + '}' 
        

q1 = Queue()
q2 = Queue()
print q1.insert(17)
q2.insert(20)
print q1.remove()
print q1
q2.remove()


#q1 = Queue()
#q2 = Queue()
#q1.insert(17)
##print q1
#q2.insert(20)
#q1.remove()
#q2.remove()
#print q1


#q = Queue()
#q.insert(1)
#q.insert(2)
#q.insert(3)
#q.insert(4)
#print q
#q.remove(3)
#print q