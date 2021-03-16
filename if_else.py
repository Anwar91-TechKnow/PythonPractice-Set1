'''
If house price is $1000
if customer having good credit then down payment will be 10%
if not then down payment will be 20%
'''
import time
price=4000 
good_credit=False
Bad_credit= True    
if good_credit:
    downPayment=0.1*price
    print("Your downPayment is ", downPayment)
elif Bad_credit:
    downPayment=0.2*price
    print("You have to paye extra ", downPayment)
    print("Sorry you dont have a good credit")
time.sleep(10)