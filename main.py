'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import time
def funa():
    print("WELCOME TO ABC LOAN SYSTEM")
    print("FIRST SCHEME OF DOWNPAYMENT AT ABC")
    price=int(input("Enter the Amount : "))
    good_credit=False
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
    elif credit=="Bad":
        down_payment1=0.2*price
        print(" Your down payment is high which is: ",down_payment1)
    else:
        print(" Unable to Process")
        print(" THANK YOU FOR USING INDIAN MORTGAGE ")
        time(20)
option =int (input("Enter the option 1 for loan 2 for dp: "))
if (option<10):
    print ("Error:!56667:Incorrect Selection Please try with correct Option----")
    time.sleep(5)
elif option==1:
        funa()
        time.sleep(20)
else:
        funa2()
        time.sleep(20)



