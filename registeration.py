import os
import re
import time
# import mainmenu

def registeration ():
    os.system("clear")
    print("--------------(Regstriation)------------------")
    FirstName = input("Enter your First Name :) ")
    while FirstName == "" or FirstName.isdigit() == True or len(FirstName) < 2:
        FirstName = input("Please Enter your First Name :) ")   

#--------------------------------------------------------------
    LastName = input("Enter your Last Name :) ")
    while LastName == "" or LastName.isdigit() == True or len(LastName) < 2:
        LastName = input("please Enter your Last Name again:) ")
#--------------------------------------------------------------
    Email = input("Enter Your Email :) ")
    while Email == "" or not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
        Email = input("please Enter your Email  again:) ")
#--------------------------------------------------------------
    Password = input("Enter Your Password :) ")
    while Password == "" or len(Password) < 6:
        Password = input("please Enter your Password again:) ")
#--------------------------------------------------------------
    ConfirmPassword = input("Confirm Your Password :) ")
    while ConfirmPassword == "" or len(ConfirmPassword) < 6 or ConfirmPassword != Password:
        ConfirmPassword = input("please Confirm your Password again:) ")
#--------------------------------------------------------------
    MobilePhone = input("Enter your Mobile Phone :) ")
    while MobilePhone == "" or MobilePhone.isalpha() == True or not re.match(r'^01[0125][0-9]{8}$', MobilePhone):
        MobilePhone = input("please Enter your Mobile Phone again:) ")
#--------------------------------------------------------------
    id =round(time.time()) 
    os.system("touch myuserdata.txt") 
    f = open("myuserdata.txt" , "a")
    f.write(f'{id}:{FirstName}:{LastName}:{Email}:{Password}:{MobilePhone}\n')
    f.close()
    os.system("clear")
    print("----------------------Success adding------------------------ ")
    
#--------------------------------------------------------------
