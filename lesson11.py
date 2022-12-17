"""
----------------------
--- Set Methods---
----------------------
"""

"""Clear()"""

a = {1, 2, 3}
a.clear()
print(a)
#
# """ Union()"""
b={'One', 'Two' ,'Three'}
c={'1','2','3'}
x={'Zero','Css'}
#print(b|c)
print(b.union(c,x))
#
# """add()"""
d={1,2,3,4}
d.add(5)
d.add(6)        # 1,2,3,4,5,6 ##Error
print(d)
#
# """ Copy()"""
#
e={1,2,3,4}
f=e.copy()
print(f)
e.add(7) #1,2,3,4
print(f)
#
# """Remove()"""
g={1,2,3,4}
g.remove(7)
print(g) #Error

"""Discard()"""

h={1,2,3,4}
h.discard(7)
print(h) #Error

"""POP()"""

i={'A',True,'Python',1,3}
print(i.pop())

"""Update()"""

j= {1,2,3,4}
t={5,6,7,8}
k={1,'A','B',2} #1,2,3,4,'A','B'
l= ["Python",'V']
print(j.update(l))