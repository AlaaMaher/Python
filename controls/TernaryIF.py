"""
----------------------
--- Ternary Conditional Operation ---
----------------------
"""
country="KSA"

if country =="Egypt":
    print('The Weather in '+country+' is 15 C')

if country =="KSA":
    print('The Weather in ' + country+" Is 25 C")
else:
    print('Country Is Not Exist Here')

age=20
movieRate=18

if age < movieRate :print("Movie is Not Good 4U")
else:print("Movie Is Good 4U")

print("Movie is Not Good 4U") if age<movieRate else print("Movie Is Good 4U")

print('The Weather in '+country+' is 15 C') if country =="Egypt" else print('Country Is Not Exist Here')

print('-'*50)
"""
----------------------
--- Calculate Age ---
----------------------
"""
# #Get Age From User
# age =input("Please Enter Your Age: ").strip()
# #Get Unit From User
# unit= input("Pls Choose Date Unit in months, weeks, days").strip().lower()
# Converting
# months= int(age)*12
# weeks= months * 4
# days= int(age)* 365
#
# if unit =="months" or unit =='m':
#     print("You Choose Months Unit  and Your age is "+ str(months))
# elif unit =="weeks" or unit =='w':
#     print("You Choose Weeks Unit  and Your age is "+ str(weeks))
# elif unit == "days" or unit == "d":
#     print("You Choose Days Unit  and Your age is "+ str(days))

"""
in 
not in 
"""

friends=['Ahmed','Abdulmalik','Yousif']
print('Ahmed'in friends)
print('Sayed' in friends)
print("Yousif" not in friends)


"""
----------------------
--- Assignment ---
----------------------
"""

"""
A small frog wants to get to the other side of the road. 
The frog is currently located at position X and wants to get to a position greater than or equal to Y. 
The small frog always jumps a fixed distance, D.
Count the minimal number of jumps that the small frog must perform to reach its target.

For example, given:

  X = 10
  Y = 85
  D = 30
the output should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100

"""
Y=85
X= 10
D=30
X2= Y-X

min=X2/D
print(min)