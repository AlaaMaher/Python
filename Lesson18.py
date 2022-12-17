"""
----------------------
--- Operators ---
----------------------
"""

"""
----------------------
--- Boolean Operators ---
and &&
or ||
not ^|
----------------------
"""
age=30
country="Egypt"
rate=10
print(age>16 and country=="USA" and rate==10) #True
print(age>16 or country=="USA" or rate==10) #True
print(not age>16) #Not True = False

print("*"*60)
"""
----------------------
--- Arthemitc Operators ---
+ 
-
*
/
%
----------------------
"""
num1=7
num2=7
print(num2%num1)

print("*"*50)
"""
----------------------
--- Assignment Operators ---
+=
-=
*=
/=
%=
----------------------
"""
x=10
y=20
z= x+y

x*=y
print(x)

print("*"*50)
"""
----------------------
--- Comparison Operators --- Return Boolean
== Equal
!= Not Equal
< Less than
> Grater Than
<= Less Than or Equal
>= Grater Than Or Equal
----------------------
"""

print(country!="USA") #False
print(num1>=num2)