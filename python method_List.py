#List method learning in python
'''
Python Collection
1. List 
2. tuple
3. set
4. Dictionery

'''
import time
print("Learning Python Collection: List ")
lst=[1,34,45,100,30,2,4]
print(lst)
var=type(lst)
print(var)
var=lst[2]
print("lst[2] ",var)
var=lst[3]
print("lst[3]",var)
var=lst[2:4]
print("lst[2:4]",var)
print(len(lst))
lst[3]=1000
lst[2]=11
var=lst
print(var)
# this is the same as per strings we can do same thing with List method
# will go through other methods
lst.insert(6,2000)# to add element at the specific position
print(lst)
lst.remove(4)#to remove specific element
print(lst)
lst.pop()# to remove last element of List
print(lst)
del lst[1] # to delete specific element of  List
print(lst)
lst.clear()
print(lst)
time.sleep(5)