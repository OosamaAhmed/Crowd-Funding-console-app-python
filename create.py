import os  
import re 
import login 
def create(x): 
    # print(f'email is {x}')
    os.system("")
    print('------------create----------------')
    Title = input("Enter Title of your Project :) ")
    while Title == "" or Title.isdigit() == True:
        Title = input("Please Enter title again :) ")   
#--------------------------------------------------------------
    Details = input("Enter Project Detail :) ")
    while Details == "" or Details.isdigit() == True or len(Details) < 10:
        Details = input("please Enter Detail of Project Agian:) ")
#--------------------------------------------------------------
    TotalTarget = input("Enter Project TotalTarget  :) ")
    while TotalTarget == "" or TotalTarget.isalpha()==True :
        TotalTarget = input("please Enter TotalTarget Agian:) ")
#--------------------------------------------------------------
    StartDate = input("Enter Start Date in this format (d/m/yyyy) :) ")
    while StartDate == "" or not re.match(r"([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})", StartDate):
        StartDate = input("Enter Start Date in this format (d/m/yyyy) :) ")
#--------------------------------------------------------------
    EndDate = input("Enter End Date in this format (d/m/yyyy) :) ")
    while EndDate == "" or not re.match(r"([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})", EndDate):
        EndDate = input("Enter End Date in this format (d/m/yyyy) :) ")
#--------------------------------------------------------------
#   i want list here 
    os.system("touch userproject.txt") 
    f = open("userproject.txt" , "a")
    f.write(f'{x}:{Title}:{Details}:{TotalTarget}:{StartDate}:{EndDate}\n')
    f.close()
    os.system("clear")
    print("---------------------- Success adding project ------------------------ ")
    
    print (" create again ??")
    print (" 1.Yes")
    print (" 2.No")
    choice = input()
    if choice == "1":
        create(x)
    elif choice == "2":
        os.system("clear")
        login.pro_menu(x)
