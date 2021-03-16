def fun1():
    sum=0
    while True:
        option=input("Select the function which you want use from given list:Sum,dedcution, division, mulfication = ")
        if option=="sum": 
                sum=a+b
                print("The Sum of two given digit is = ",sum)
                time.sleep(20)
        elif option=="dedcution":
            c=a-b
            print("The dedcution of two given digit is = ",c)
            time.sleep(20)
        elif option=="division":
            d=a/b
            print("The division of two given digit is = ",d)
            time.sleep(20)
        elif option=="multification":
            e=a*b
            print("The mulfication of two given digit is = ",e)
            time.sleep(20)
        else:
            print("  Error Code:D44rd >>>>>>>Please use correct option<<<<<<<  ")
            continue
            time.sleep(10)