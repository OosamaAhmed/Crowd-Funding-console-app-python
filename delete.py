import login

def delete(x):
    print("-------------- Delete Project ---------------------")
    delete_project= input("Enter Name of project to delete :) ")
    f = open("userproject.txt", 'r')
    lines = f.readlines()
    f.close()
    new_data = []
    for line in lines:
        line = line.split(":")
        if not (line[1] == delete_project and line[0] == x):
                line = ":".join(line)  #return line that wasn't deleted
                new_data.append(line)
        else:
           print("Project deleted successfully")

                
    f = open("userproject.txt", 'w')
    f.writelines(new_data)
    f.close()

    login.pro_menu(x)
