"""
----------------------
--- Set ---
----------------------
[1] Set Items Are Enclosed In Carly Braces
[2] Set Items Are Not Ordered, Not Indexing
[3] Set Indexing And Slicing Can't Be Done
[4] Set Has Only Immutable Data Types ( Numbers, Strings,Tuple) List and Dis Are Not
[5] Items Are Unique
"""

MySetOne={'Ahmed', 'AbdelMalik','One',True}
#print(MySetOne[0]) #Error

# MyListOne=['Ahmed', 'AbdelMalik','One',True]
# print(MyListOne[1:3])
# #
# MyTupleOne=('Ahmed', 'AbdelMalik','One',True)
# print(MyTupleOne[1:3])

"""Set Has Only Immutable Data Types"""

# MySetThree= {"Ahmed", "AbdelMalik",100,100.5,True,[1,2,3,4]}
# print(MySetThree) #unhashable type: 'list'

# MySetFour= {"Ahmed", "AbdelMalik",100,100.5,True,(1,2,3,4)}
# print(MySetFour)

"""Items Are Unique """

MySetFive={1,2,3,"AbdelMalik","One","AbdelMalik",1,"Ahmed",2,"One",True}
print(MySetFive)    # 1,2,3,AbdelMalik,One,Ahmed, True

MyListFive=[1,2,3,"AbdelMalik","One","AbdelMalik",1,"Ahmed",2,"One",True]
print(MyListFive)

MyTupleFive=(1,2,3,"AbdelMalik","One","AbdelMalik",1,"Ahmed",2,"One",True)
print(MyTupleFive)