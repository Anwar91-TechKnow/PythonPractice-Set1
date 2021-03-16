#changing class/type of values in Python

print("before conversion")
x = 1 # int")
y = 2.8 # float
z = 1j # complex

print("x =",x,type(x))
print("y =",y,type(y))
print("z =",z,type(z))

print("After conversion")
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(x)

print("x =",x,type(x))
print("y =",y,type(y))
print("z =",z,type(z))
