import os
import create
def edit(x):
    os.system("clear")
    print('---------------------edit-------------------------')
    edit_userd=input ("Enter project name to Edit it :) ")
    f = open("userproject.txt", 'r')
    lines = f.readlines()
    f.close()
    new_data = []
    for line in lines:
        line = line.split(":")
        if not (line[1] == edit_userd and line[0] == x):
                line = ":".join(line)  #return line that wasn't deleted
                new_data.append(line)
        else:
           print("Project deleted successfully now you can  Enter your new project Data")

                
    f = open("userproject.txt", 'w')
    f.writelines(new_data)
    f.close()
    create.create(x)