'''When you know that Values are not going to change then use tuple
e.g roll number, Employee number
When you know that values are gonna change then use List
e.g Marks
Set has only unique element
and not follow the sequence
'''
import time
a=[1,2,'three',45,100]
print(a)
b={1,2,'three',45,100}
print(b)
c=(1,2,'three',45,100)
print(c)
print("type A",type(a))
print("type B",type(b))
print("type C",type(c))
time.sleep(5)