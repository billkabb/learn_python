# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:26:13 2016

@author: billkabb
"""
#def FancyDivide(numbers, index):
#    try:
#        denom = numbers[index]
#        for i in range(len(numbers)):
#            numbers[i] /= denom
#    except IndexError, e:
#        FancyDivide(numbers, len(numbers) - 1)
#    except ZeroDivisionError, e:
#        print "-2"
#    else:
#        print "1"
#    finally:
#        print "0"
#def FancyDivide(numbers, index):
#    try:
#        try:
#            denom = numbers[index]
#            for i in range(len(numbers)):
#                numbers[i] /= denom
#        except IndexError, e:
#            FancyDivide(numbers, len(numbers) - 1)
#        else:
#            print "1"
#        finally:
#            print "0"
#    except ZeroDivisionError, e:
#        print "-2"
#def FancyDivide(list_of_numbers, index):
#    try:
#        try:
#            raise Exception("0")
#        finally:
#            denom = list_of_numbers[index]
#            for i in range(len(list_of_numbers)):
#                list_of_numbers[i] /= denom
#    except Exception, e:
#        print e
def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"          
          
FancyDivide([0, 2, 4], 0)