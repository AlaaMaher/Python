from operator import*

"""
----------------------
--- Loop ---> For Training ---
----------------------
----------------------
"""

"""Range()"""

# myRange=range(1,101)
#
# for num in myRange:
#     print(num)

"""Dictionary"""

# mySkills={"Java":"99%","Kotlin":"100%","Python":"80%","CSS":"70%"}
#
# print(type(mySkills))
# print(mySkills.get("Kotlin"))
# print(mySkills["Python"])
# print(mySkills["CSS"])
#
# for skill in mySkills:
#      print(f"My Level in {skill} - {mySkills.get(skill)}")





"""
----------------------
--- Nested Loop ---> For ---
----------------------
----------------------
"""

# students=["Ahmed","Abdmalik","Mohamed","Yousif","Soha"]
# subjects=["Arabic","English","Science","Math"]
#
# for name in students: #outer loop
#     print(f"{name} study :")
#     for sub in subjects: #inner loop
#         print(sub)

"""Dic"""

# students={
#     "Ahmed":{"Arabic":"99%","English":"98%"},
#     "Yousif":{"Math":"95%","Science":"100%"},
#     "Abdmalik":{"Python":"99%","Xml":"0%"}
# }

# print(students["Ahmed"])
# print(students["Yousif"])
# print(students["Abdmalik"])
# print(students["Ahmed"]["Arabic"])
# print("*" * 50)
# print(students["Abdmalik"]["Xml"])
#
# for student in students:
#     print(f"Subjects for {student} is ")
#     for sub in students[student]:
#         print(f"The Result of {sub} is {students[student][sub]}")

"""
----------------------------------
--- Break---- Continue ----Pass
----------------------------------
----------------------------------
"""
# MyNumbers=[1,2,3,5,7,10,13,14,15,19]
#
# for num in MyNumbers:
#     if num == 13:
#         pass



"""
----------------------
--- Assignment ---

Given a list of numbers, write a program to find the sum of all the elements in the list using three methods 
1- For Loop with range 
2- While 
3 - Add as BuildIn Function --> plus

Example:  
Input: [12, 15, 3, 10]
Output: 40

Input: [17, 5, 3, 5]
Output: 30

----------------------
----------------------
"""
#1
# sum =0
list= [12, 15, 3, 10]
#
# myrange= range(0,len(list))
# print(myrange)
# for element in myrange:
#     sum = sum + list[element]
# print(sum)

#2
# sum=0
# element=0
# while element < len(list):
#     sum = sum + list[element]
#     element +=1
# print(sum)

#3 Using Add Function from Operator Module

sum =0
for element in list:
    sum = add(element,sum)
print(sum)


