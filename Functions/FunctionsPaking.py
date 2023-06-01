"""
--------------------------------------------------
--- Function Parameters & Arguments---
--------------------------------------------------
--------------------------------------------------
def    --->  Function Keyword defined
sayHello  --> name
name ---> Parameter
Ahmed --> Argument
task ---> print Hello
"""

# list = [1, 2, 3, 4]
# print(*list)


# def sayHello(*people):
#     print(type(people))
#     for name in people:
#         print(f"Hello {name}")
#
# mySkills={
#     "Java":"70",
#     "Python":"60",
#     "Kotlin":"90%"
# }
#
# def showSkills(**skills):
#     print(type(skills))
#     for skill_key, skill_value in skills.items():
#         print(f"your Skills is {skill_key} ---> {skill_value}")
#
# showSkills(Python="50%", Java="90%")
# showSkills(**mySkills)


# sayHello("Alaa", "Ahmed", "AbdMalik", "Fedaa", "Arwa", "Alaa", "Sondos", "Mohamed")

#
# a, b, c, d = "Ahmed", "Alaa", "Abdelmalik", "Yousif"
#
# # print(f"Hello {a}")
# # print(f"Hello {b}")
# # print(f"Hello {c}")
# # print(f"Hello {d}")
#
# #
# # def sayHello(name):
# #     print(f"Hello {name}")
# #
# #
# # def add(num1,num2):
# #     return num1+num2
# #
# # sayHello("Ahmed",14)
# #
# # print(add(3,4))
# """
# --------------------------------------------------
# --- Function Packing, Unpacking Arguments *Args---
# --------------------------------------------------
# --------------------------------------------------
# """
#
# print(1, 2, 3, 4)
# myList = [1, 2, 3, 4]
# print(*myList)
#
#
# def sayHello(*people):
#     for username in people:
#         print(f"Hello {username}")
#
#
# sayHello("")
#
"""
--------------------------------------------------
--- Function Default Parameters---
--------------------------------------------------
--------------------------------------------------
"""


def sayHello(name="Unknown", age="Unknown", country="Unknown"):
    print(f"Hello {name} , Your age is  {age}, Your Country is {country}")


sayHello("Aalaa")
sayHello()

# def sayHello(age="15",country="Egypt",*people):
#     for name in people:
#      print(f"Hello {name} and your age is {age},from {country}")
#
# sayHello("Ali","Ahmed","Alaa")
#
# """
# ------------------------------------------------------
# --- Function Packing, Unpacking Arguments ** KWArgs---
# ------------------------------------------------------
# ------------------------------------------------------
# """
#
#
# # mySkills={
# #     "Java":"70",
# #     "Python":"60",
# #     "Kotlin":"90%"
# # }
#
# def showSkills(**skills):
#     print(type(skills))
#     for skillKey, skillValue in skills.items():
#         print(f"Your Skills is {skillKey} ---> {skillValue}")
#
#
# showSkills(Html="50%",Css="60%",Python="70%")
