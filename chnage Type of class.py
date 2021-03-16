#change the type of variables\\
import time
a=34.33
b='Anwar'
c=23
d=59.3
#before changes the type
print("before")
print("(a) = ",a, type(a))
print("(b) = ",b, type(b))
print("(c) = ",c, type(c))
print("(d) = ",d, type(d))
#after changes the type
print("After")
a=type(int)
b=type(float)
c=1.1
d=type(str)
print(type(a))
print("(a) = ",a, type(a))
print("(b) = ",b, type(b))
print("(c) = ",c, type(c))
print("(d) = ",d, type(d))