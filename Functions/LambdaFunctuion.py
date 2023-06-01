"""
--------------------------------------------------
--- Lambda Function ---
---Anonymous Function----
--------------------------------------------------
[1] It has no name
[2] You can call it inline without defining it
[3] You can Use it to return data from another function
[4] Used For Simple Functions
[5]It is Single Expression not a block of code
[6] Lambda Type ---> Function
"""


def say_hello(name,age): return f"Hello {name}, and Your age is {age}"

print(say_hello("Abdmalik",14))

hello = lambda name,age: f"Hello {name}, and Your age is {age}"
print(hello("Ahmed",14))
print(type(hello))

print(say_hello.__name__)
print(hello.__name__)


x= lambda a:a+5

print(x(5))


def myFun(n):
    return lambda a:a*n

doubleNum= myFun(2)
triple= myFun(3)
print(doubleNum(11))
print(triple(3))







"""
----------------------
--- Assignment ---
----------------------
Write a lambda function that return plus two numbers
"""