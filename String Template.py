#Uses of templete functionality in string
import time
str='This is a'
name1="Anwar"
name2="Shaikh"
name3="Ravi"
str2="This is bad boy"
temp="This is a {2} and he is bad boy{0}".format(name1,name2,name3)
print(temp)
time.sleep(3)
#Another example
#Uses of templete functionality in string
import time
str='This is a'
name1="Anwar"
name2="Shaikh"
name3="Ravi"
str2="This is bad boy"
#temp="This is a {2} and he is bad boy{0}".format(name1,name2,name3)
temp=(f"This is a {name1} and he is bad boy {name3} and {name3})
print(temp)
time.sleep(15)