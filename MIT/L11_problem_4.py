# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:26:13 2016

@author: billkabb
"""
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        # First make sure `other` is of the same type 
        assert type(other) == type(self)
        # Since `other` is the same type, test if coordinates are equal
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'
        
class Point3D(object):
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c
    def __repr__(self):
        return "Point3D(%d, %d, %d)" % (self.x, self.y, self.z)
    def __str__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print `my_point` # __repr__ gets called automatically
print my_point # __str__ gets called automatically



            
x = 123
y = 123
c = Coordinate(x,y)
c2=eval(repr(c))
print c
print `c` 
print str(c)
print c2
print eval(`c`)
print c.__eq__(c2)
#print c