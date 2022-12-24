"""
----------------------
--- Control Flow ---
   If, Elif, Else, Nested If
----------------------
"""

isStand= True

"""if Condition : """

if isStand :
    print("He Is Stand Now")


isCold= False

if isCold :
    print("Wear Jacket")
else:
    print('Do not Wear Jacket')

num=7

if num == 4: print(num)
elif num ==5: print("Num equal 5")
elif num ==7:
    print("Num Equal 7")
else: print("Num Does not Exist")


l=[7,4,2,9,3]

max= l[0]

if l[1] > max: max=l[1]
if l[2]>max:
    max =l[2]
if l[3]>max:
    max = l[3]
if l[4]>max:
    max=l[4]
    print(max)
else:print(max)

#Minimum Program

# Finding The missing number of any list 5 length [1,2,4,5] Without using Loops



