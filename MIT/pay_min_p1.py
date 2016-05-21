
balance=input("Please enter balance >>>")
rembalance=balance
annualInterestRate=input("Please enter the annual interest rate 'e.g 0.18 for 18%' >>>")
monthlyInterest=annualInterestRate/12.0
monthlyPaymentRate=input("Please enter the monthly payment rate 'e.g 0.18 for 18%' >>>")
month=12
#totalPaid=0
subtotal=0
monthlyTotal=0

for m in range(month):
    
    monthly=balance*monthlyPaymentRate#0.02
    
    #monthlyNew=newBalance*monthlyPaymentRate
    monthlyInt=monthlyInterest#0.18/12
    rembalance=balance-(balance*monthlyPaymentRate)
    newBalance=balance-(balance*monthlyPaymentRate)+(rembalance*monthlyInt)
    interest=rembalance*monthlyInt
    #print subtotal+interest
    print "month:",m
    #print "new balance: ",newBalance
    print "balance:",round(balance,2),"\nMinimum monthly payment:",round(monthly,2),"\nRemaining balance:",round(newBalance,2),"\ninterest:",round(rembalance*monthlyInt,2),"\n----"
    #print interest
    #subtotal=interest
    #print subtotal
    #totalPaid=round(subtotal+interest,2)
    #print "Total interest: ",totalPaid
    subtotal=subtotal+interest
    monthlyTotal=monthlyTotal+monthly
    balance=balance-(balance*monthlyPaymentRate)+(rembalance*monthlyInt)

print "Total paid interest: ",round(subtotal,2)
print "Total paid: ",round(monthlyTotal,2)
print "Total Remaining balance:",round(newBalance,2)



##########################################
##balance=input("Please enter balance >>>")
##rembalance=balance
##annualInterestRate=input("Please enter the annual interest rate 'e.g 0.18 for 18%' >>>")
##monthlyInterest=annualInterestRate/12.0
##monthlyPaymentRate=input("Please enter the monthly payment rate 'e.g 0.18 for 18%' >>>")
##month=12
##totalPaid=0
##
##for m in range(month):
##    
##    monthly=balance*monthlyPaymentRate#0.02
##    monthlyInt=monthlyInterest#0.18/12
##    rembalance=balance-(balance*monthlyPaymentRate)
##    
##    print "month:",m
##    print "balance:",round(balance,2),"\nMinimum monthly payment:",round(monthly,2),"\nRemaining balance:",round(rembalance,2),"\ninterest:",round(rembalance*monthlyInt,2),"\n----"
##    
##    balance=balance-(balance*0.02)+(rembalance*monthlyInt)
############################################################


##Month: 1
##Minimum monthly payment: 96.0
##Remaining balance: 4784.0

##Total paid: 96.0
##Remaining balance: 4784.0
#monthly=balance*0.02
    #rembalance=(balance-(balance*0.02))+(balance*monthlyInt)
    #print rembalance*monthlyInt
    #print "balance:",balance
    #print round(monthly,2)
    #print "interest:",rembalance*monthlyInt
