#First Sucessed programme:

'''
'''
import time
def funa():
#"""This is the funtion i have crated for Mortage"""
    print("WELCOME TO ABC LOAN SYSTEM")
    print("FIRST SCHEME OF DOWNPAYMENT AT ABC")
    price=int(input("Enter the Amount : "))
    good_credit=True
    Bad_credit= False 
    if good_credit:
        downPayment=0.1*price
        print("Your downPayment is ", downPayment)
    else:
        downPayment=0.2*price
        print("You have to paye extra ", downPayment)
        print("Sorry you dont have a good credit")


def funa2():
    print("SECOND SCHEME OF DOWNPAYMENT AT ABC")
    print("Welcome To ABC Mortage")
    price=int(input ("Enter the Amount : "))
    credit="good"
    if price>1000:
        if credit=="good":
             down_payment1=0.1*price
        print ("Your Down payment is: ",down_payment1)
    elif credit=="good":
        down_payment1=0.2*price
        print(" Your down payment is high which is: ",down_payment1)
    else:
        print(" Unable to Process")
        print(" THANK YOU FOR USING INDIAN MORTGAGE ")

print(funa)
option =int (input("Enter the option 1 for loan 2 for dp: "))
if option==1:
        funa()
        time.sleep(10)
else:
        funa2()
        time.sleep(10)