"""
----------------------
--- Dictionary Methods ---
----------------------
"""

"""setdefault()"""

user={'name':'Ali'}
print(user)
print(user.setdefault('age',36))
print(user)

print("-"*40)

"""PopItem()"""
member={'name':'Ali','skill':'Python'}
print(member)
member.update({'age':36})
print(member.popitem())

print("-"*40)


"""items()"""
Game={'name':'Apex','rank':'Gold'}
allItems=Game.items()
print(Game)
Game['main']='nami'
print(allItems)

print("-"*40)

"""FromKeys()"""

a=('KeyOne','KeyTwo','KeyThree')
b='x'
dict=dict.fromkeys(a,b)
print(dict)
print("-"*40)

"""Boolean"""
name=' '
print(name.isspace())
print(100>200)
print(100>100)
print(100>90)
print("-"*40)

"""bool"""

"""True"""
print(bool("Ahmed"))
print(bool(100))
print(bool(100.97))
print(bool(True))
print(bool([1,2,3,4]))

"""False"""
print(bool(""))
print(bool(0))
print(bool(False))
print(bool(None))
print(bool([]))