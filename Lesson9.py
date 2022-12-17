"""
----------------------
--- Tuple ---
----------------------
[1] Tuple Items Are Enclosed In Parentheses
[2] You Can Remove The Parentheses
[3] Tuple Are Ordered, Use Index To Access Items
[4] Tuple Are Immutable ---> Can't Edit, Delete, Add
[5] Tuple Items Are Not Unique
[6] Can Have Different Data Types
[7] Operators Used in Strings and Lists are In Tuple
"""

"""Syntax & Test"""

myTupleOne = ('Ahmed', 'AbdelMalik', True, 1, 2)
myList = ['Ahmed', 'AbdelMalik']
print(type(myTupleOne))

myTupleTwo = 'Ahmed', 'AbdelMalik'
print(type(myTupleTwo))

"Indexing Access Tuple"
myTupleThree = 'Ahmed', 'AbdelMalik'
print(myTupleOne[2])  # True

friends = ["Ahmed", "Ali", "Omar", "Abdumalik"]
myOldFriends = ["Maged", "Basem", "Mohamed", "Moaz"]
friends.extend(myOldFriends)
print(friends)

myTupleFour = ('Ahmed', 'Ahmed', 'AbdelMalik', True, 1, 2)
print(myTupleFour[0:2])

"""Tuple With One Element"""
myTupleFive = ("Alaa",)
myTupleSix = "Alaa",
print(type(myTupleFive))
print(type(myTupleSix))  # Expexted <class 'tuple'>
print(len(myTupleFive))
print(len(myTupleSix))

"""Tuple Concatenation"""
a = (1, 2, 3, 4)
b = (5, 6)
c = b + a
print(c)  # (1, 2, 3, 4,5,6)

"""Tuple, List, String Repeat(*)"""

myString = 'Abdulmalik'
myList = [1, 2]
myTuple = ('A', 'B')

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

"""Methods"""
""" Count"""
a1 = (1, 3, 7, 8, 2, 6, 5, 8)
print(a1.count(8))  # 2

"""index"""
b1 = (1, 3, 7, 8, 2, 6, 5)
print(b1.index(7))  # 2

""" Tuple Destruct"""
a2 = 'H','J', 'K','T'

_, x, y,z = a2 #Error
print(x)
print(y)
print(z)


""" Declare Two Tuple 
 1-  Concatenation between Them
  2- repeat First Tuple
  3- Destruct second Tuple with A,B,C Strings"""
