import os
import create 
import edit
import delete
import view

#  users = readFile.readlines()

os.system("")
print("--------------(Login)------------------")

def get_user(Email,password):
    
    f = open("myuserdata.txt", 'r')
    lines = f.readlines()
    f.close()
    # print(lines)
    for line in lines:
        mylist = line.split(':')#return list 
        # print(f'------------mylist is{mylist}')
        # mylist is['1676400070', 'osama', 'ahmed', 'osama@gmail.com', '123456', '01066000903\n']
        if mylist[3] == Email and mylist[4] == password  :
            return mylist[0] 
    else:
        return False


def login():
    
    Email = input("Enter Your Email:) ")
    password = input("Enter Your Password:) ")
    while not get_user(Email, password):
        print("try again...")
        Email = input("Enter Your Email:) ")
        password = input("Enter Your Password:) ") 
    x=get_user(Email, password) #getting user id 
    # print(x)
    # os.system("clear")
    print("------------login successful-------------")
    pro_menu(x)

def pro_menu(x):
    print("--------------(Pro Menu)------------------")
    print("1. Create Project")
    # print("2. View Project")
    print("2. Edit Project")
    print("3. Delete Project")
    print("4. Exit")
    
    choice = input("Enter Your Choice:) ")
    if choice == "1":
        create.create(x)
        
    elif choice == "2":
        edit.edit(x)
    
    elif choice == "3":
        delete.delete(x)
    
    elif choice == "4":
        exit(x)
    else:
        print("Invalid choice please try again :)")
    os.system("clear")
