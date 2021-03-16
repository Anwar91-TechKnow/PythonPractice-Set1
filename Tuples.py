'''
Tuple Learning in python
# When you know that Values are not going to change then use tuple
e.g roll number, Employee number
'''
import time
tup=(1,2,4,88,33,883,3) #tuple with pathenerless
print(tup)
print(type(tup))
tup2='Anwar','Shaikh','Subhash','Nilesh' #tupe withouth pathenerless
print(tup2)
print(type(tup2))
tup3=tup+tup2 #combining Tuples
print(tup3)
tup3=tup,tup2 #additon of tuples
print(tup3)
print(len(tup2))
print(len(tup))
tup3=()
print(tup3) #blank tuple
print(tup[2])
print(tup[6])
print(tup[2:6]) #slicing of tuple
del tup3 #deleting blank tuple
print(tup2*2)#multiple tuple
print(5 in tup2)
print('Anwar' in tup2) #to validate whether element is available or Not 
print(max(tup2))
print(min(tup)) #min and max function in tuple
# tuple packing and unpacking
a=('Anwar',28,'Hyderabad',1991,'Pune') #tuple packing
(Name,Age,HomeTown,BirthYear,CurrentCity)=a #tuple unpacking
print("Name Is: " ,Name,"\n","Age of Anwar",Age,"\n",HomeTown,"\n",BirthYear,"\n",CurrentCity,"\n")

#case packing and unpacking of tuple 
T = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
(Name,NickName,Year,MovieName,Profession,state)=T
print(Name,"\n",NickName,"\n",Year,"\n",MovieName,"\n",Profession,"\n",state,"\n")
T2 = (1,2,3,4,5,6,7);
print(T[0])
print(T2[1:4])
print(T+T2) #addition of twp tuples
time.sleep(5)