#Problem 2: Paying Debt Off in a Year
balance=input("Please enter balance >>>")
annualInterestRate=input("Please enter the annual interest rate 'e.g 0.18 for 18%' >>>")
monthlyInterest=annualInterestRate/12
paid=10
month=12

##while True:
##    remain = balance
##    for i in range(12):
##        remain = (remain - paid )+(remain-paid ) * ( annualInterestRate / 12.0)
##        print i,paid,remain 
##        #print (1+ annualInterestRate / 12.0)
##    if remain > 0:
##        paid += 10
##    else:
##        break
##    
##print 'Lowest Payment:', paid

while True:
    total=balance
    for m in range(month):
        
        total= (total-paid)+(total-paid)*monthlyInterest
    ##    print (balance+(balance*annualInterestRate)-(paid*13))
        #print paid
    if total>0:
        paid+=10
    else:
        break
    
##    
print "Lowest Payment: ",paid
##
##print "bal_1",3329+(3329*0.2)
##print "paid",310
##print "x13",310*13
##
##print "bal_2",4773+(4773*0.2)
##print "paid",440
##print "x13",440*13
##
##print "bal_3",3926+(3926*0.2)
##print "paid",360
##print "x13",360*13

##
##fixed = 10
##
##while True:
##    remain = balance
##    for i in range(1, 13):
##        remain = (remain - fixed) * (1 + annual / 12.0)
##    if remain > 0:
##        fixed += 10
##    else:
##        break
##    
##print 'Lowest Payment:', fixed








