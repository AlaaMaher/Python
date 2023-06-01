"""
--------------------------------------------------
--- Function Scope ---
--------------------------------------------------
Global Scope
Local Scope
--------------------------------------------------
"""

# x=1
# print(f"The Variable From Global Scope {x}")
#
#
#
# def one():
#     x=2
#     print(f"The Variable Inside Function {x}")
#
# def two():
#     global x
#     x=3
#     print(f"The Variable From Local {x}")








# one()
# two()
# print(f"The Variable From Global Scope {x}")


"""
----------------------
--- Assignment ---
----------------------

x = 50

def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)



The Output of the Following is 


A)
x is 50
Changed global x to 2
Value of x is 50

B)
x is 50
Changed global x to 2
Value of x is 2

C)
x is 50
Changed global x to 50
Value of x is 50

"""
