"""
----------------------
--- Lists ---
----------------------
[1] List Items Are Enclosed square Items
[2] List Are Ordered, To use Index To access it
[3] List Are Mutable ---> add, delete, edit
[4] List Items are Not Unique
[5] List can Contain Different Data Types
"""
name=[]
myAwesomeList = ["Ali", 1, True, "Ali"]
friends = ["Ahmed", "Ali", "Omar", "Abdumalik"]
myOldFriends = ["Maged", "Basem", "Mohamed", "Moaz"]

# print(friends[1:3]) #Ali,omar
# print(friends[:4]) #"Ahmed","Ali","Omar"
# print(friends[1:]) #"Ali","Omar","Abdumalik"
# "Abdumalik","Omar","Ali"

# print(friends[::1])

friends[2] = "Mahmoud"  # "Ahmed","Ali","Mahmoud","Abdumalik"
# print(friends)
# print(myAwesomeList)

"""Methods
append()
"""
friends.append(myOldFriends)  # "Ahmed","Ali","Omar","Abdumalik", ["Maged","Basem","Mohamed","Moaz"]
friends[4] = "Haitham"
print(friends)
# print(type(friends[3]))

"""extend()"""

friends.extend(myOldFriends)
print(friends)

character_name = "Ahmed"
age = "14" 'A'
print()

# int long
# ch   String


"""Ignore this"""
