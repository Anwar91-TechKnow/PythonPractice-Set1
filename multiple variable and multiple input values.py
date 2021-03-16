# #multiple varibale how to add into python program
# print("Provide inputs by seperating by comma")
# name,age='Anwar', '24'
#     print("Your name is "+name,"and your age is "+age)

#multiple input values together
import time
print("Provide inputs by seperating by Space")
Name,Age=input("Enter Your name and age ").split()
print(Name)
print(Age)

#multiple input values together
print("Provide inputs by seperating by comma")
Name1,Age1=input("Enter Your name and age ").split(",")
print(Name1)
print(Age1)
time.sleep(5)