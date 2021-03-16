#second example where continue and break both used:
import time
sum=0
while (True):
        inp=int(input("Enter The Number"))
    if inp>100:
        print("Congracts you have entered number greater than 100")
        break
    else:
        print("Try Again")
        continue