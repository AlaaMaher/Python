"""
----------------------
--- Practical Controls ---
----------------------
"""

"""List Contain Admins"""

admins=['Ahmed','Abdmalik','Yousif','Alaa']

#Login
userName=input("Please Enter Your User Name :").strip().capitalize()
if userName in admins:
    option= input("Remove Or Update : ").strip().capitalize()
    if option == 'Update':
        NewName= input("Please Enter Your New User Name : ").strip().capitalize()
        admins[admins.index(userName)]=NewName
        print(admins)

    elif option == 'Remove' or option == 'R':
        admins.remove(userName)
        print("Admin Deleted")
    else:
        print("Option Not available")
else:
 status= input("Not Admin, Add You, Y,N?").strip().capitalize()
if status == 'Y' :
  admins.append(userName)
print(admins)


























""""Write A Program That check if a Canary is in a list of animals list  and delete it"""