"""
--------------------------------
--- Advanced Dictionary Loop ---
--------------------------------
--------------------------------
"""

mySkills = {"Java": "99%", "Kotlin": "100%", "Python": "80%", "CSS": "70%"}
# for skill in mySkills:
#     print(f"{skill} --> is {mySkills[skill]}")

# print(mySkills.items())
# for key, value in mySkills.items():
#     print(f"{key} is {value}")


"""
--------------------------------
---2D Advanced Dictionary Loop ---
--------------------------------
--------------------------------
"""

students = {
    "Ahmed": {"Arabic": "99%", "English": "98%"},
    "Yousif": {"Math": "95%", "Science": "100%"},
    "Abdmalik": {"Python": "99%", "Xml": "0%"}
}
#print(students.items())

# for student in students:
#     print(student)
#     for sub in students[student]:
#         print(sub)

for main_key , main_value in students.items():
    print(f"{main_key}")
    for child_key, child_value in main_value.items():
        print(f"{child_key} ----> {child_value} ")
