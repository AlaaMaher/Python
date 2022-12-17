"""
----------------------
---  Two Dimensional Dictionary ---
----------------------
"""

languages = {"One": {'name': 'Python', 'expert': "20%"},
             "Two": {'name': 'Css', 'expert': '40%'},
             "Three": {'name': 'JS', 'expert': '10%'}}
print(languages)
print(languages['One']['expert'])

"""Collect Dic In One"""

FrameWork1 = {'name': 'Spring'}
FrameWork2 = {'name': 'Angular'}
FrameWork3 = {'name': 'Flutter'}

allFrameWork = {'One': FrameWork1, 'Two': FrameWork2, 'Tree': FrameWork3}
print(allFrameWork)

print("*"*50)
"""
----------------------
--- Dictionary Methods ---
----------------------
"""
"""Clear()"""
user={'name':'Alaa'}
print(user)
user.clear()
print(user)
print("*"*50)

"""update"""
member={'name':'Alaa'}
print(member)
member['age']= 29
print(member)
member.update({'name':'Ali'})
print(member)
print("*"*50)

"""Copy()"""
main={'name':'AbdulMalik'}
d= main.copy()
print(d)
main.update({'skills':'Python'})
print(main)
print(d)
print("*"*50)

"""keys & values"""
print(main.keys())
print(main.values())