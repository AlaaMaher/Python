"""
----------------------
--- Loop ---> While ---
----------------------
--- Simple Bookmark Manage ---
----------------------
--- Simple Password Guess ---
----------------------
"""

"""Simple Bookmark Manage"""


#Empty List For my Fav Websites

myFavWeb=[]
#max num of webs

maxNumWeb=5
while maxNumWeb > 0:
  web = input('Domain Name Without https:// ')
  myFavWeb.append("https://"+web.strip().lower())
  maxNumWeb -=1 #  maxNumWeb = maxNumWeb-1
  print("Website Added, "+str(maxNumWeb)+"places")
  print(myFavWeb)
else:
    print("Bookmark is Full, You can't add more")
    if len(myFavWeb)>0:
        myFavWeb.sort()
        print("Your Bookmark List")
        index=0
        while index <len(myFavWeb):
            print(myFavWeb[index])
            index +=1


"""Simple Password Guess"""
"""Game Revive Program """



