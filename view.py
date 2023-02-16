import os 
import login 
def view(x):
    os.system('clear')
    print('------------- viewing all project data ------------------')
    os.system('cat userproject.txt')
    print (" Exit or minu project  ??")
    print (" 1.Exit ")
    print (" 2. minu project ")
    choice = input()
    if choice == "1":
        exit()
    elif choice == "2":
        login.pro_menu(x)



