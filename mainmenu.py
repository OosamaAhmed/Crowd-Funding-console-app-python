import registeration
import login
import os 
import view
def main_menu():
    os.system("clear")

    while True:
        print("------------------ Main Menu -----------------")
        print ("1. registering..")
        print ("2. login..")
        print ("3. veiw all pro ..")
        print ("4. Exit..")

        choice = int(input("Enter your choice :) "))
        if choice == 1:
            registeration.registeration()
        elif choice == 2:
            login.login()
            break
        elif choice == 3:
            view.view()
        elif choice == 4:
            exit()
        else:
            print("Invalid choice please try again :)")
    
main_menu()