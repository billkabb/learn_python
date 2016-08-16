# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:16:53 2016

@author: billkabb
"""
'''
def f(a, b):
    #return "a + b"
    return "a > b"


def dict_interdiff(d1, d2):
    tup1 = ()
    tup2 = ()
    dic1 = {}
    dic2 = {}
    if f(a, b) == "a + b":
        
        for i in (d1.keys() + d2.keys())  :
            try:
                if i not in dic1:
                    dic1[i]=d1[i]+d2[i]
                
            except KeyError:
                
                if i in d1.keys():
                    dic2[i]= d1[i] 
                elif i in d2.keys():
                    dic2[i]=d2[i]
        tup1= (dic1,dic2)
        return tup1
                 
    if f(a, b) == "a > b":        
        
        
        for i in (d1.keys() + d2.keys())  :
            try:
                if d1[i] and d2[i]:
                    dic1[i]=False    
            
            except KeyError:
#                
                if i in d1.keys():
                    dic2[i]= d1[i] 
                elif i in d2.keys():
                    dic2[i]=d2[i]
        tup2= (dic1,dic2)
        return tup2
'''
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # inter: dictionary. keys: keys that are common in both d1 and d2.
    # values: result of applying f to values of inter's keys.
    inter = {}
    # diff: dictionary with only d1 elements and only d2 elements 
    diff = {}

    for key in d1.keys():
        if key in d2:
            inter[key] = f(d1[key], d2[key])
        else:
            diff[key] = d1[key]

    for key in d2:
        if key not in inter:
            diff[key] = d2[key]

    return (inter, diff)
    
#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
a = ""
b=""
print f(a, b)
print dict_interdiff(d1, d2)