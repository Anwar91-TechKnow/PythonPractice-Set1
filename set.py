'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#Learning Sets in python
'''
1.A set is a collection which is unordered and unindexed
2.Sets are unordered, so you cannot be sure in which order the items will appear.
3.you can not access value of Sets however you can find the items in Sets
4.Set writ in the curly bracess.
5.Once a set is created, you cannot change its items, but you can add new items
6.If the item to remove does not exist, discard() will NOT raise an error.
7.remove will trough an error if trying to remove item which is not in the set


'''
import time
a={"School","Notebook","Pen","Classroom"} #variable 1
print(a)
print(type(a))
print("Classroom" in a) #True
print("teacher" in a) #False
print(a)
b={"Banana","Almond","Apple","Grapes"} #variable 2
print(b)
print(a,b)
#adding one item into set
a.add("Student")
print(a)
#adding multiple items more than 1 
b.update(["Mango","Orrage","Pears"])
print(b)
#getting lenth of set
print(len(a));print(len(b))
a.remove("Student") #remove element from set
print(a)
b.discard("Mango") # dicard also can use to remove element in set
print(b)
time.sleep(10)