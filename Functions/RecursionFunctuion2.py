"""
--------------------------------------------------
--- Recursion Function Part 2 ---
--------------------------------------------------
 A Function is said to be recursive if it calls itself
"""

"""
--------------------------------------------------
Remove duplicate character from given string using Recursion Like [ WWWoooorrrlllddd] return World
"""



# def clearword(s):
#     if len(s)==1:
#         return s
#     print(f" Word Before Condition  {s}")
#     if s[0] ==s[1]: #WWWoooorrrlllddd
#      return clearword(s[1:]) #Woooorrrlllddd
#     print(f" Word After Condition  {s}")
#     return s[0]+clearword(s[1:])
#
# print(clearword("WWWoooorrrlllddd"))


"""
Fibonacci Numbers


0,1,1,2,
0,1,1,2,3,5,8,13,21,......

"""

def Fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return Fib(x-1)+Fib(x-2)

print(Fib(7))




"""
Recursion  VS Iteration

"""

"""
----------------------
--- Assignment ---
----------------------
Calculate the sum of numbers from 1 to n using recursion.
 The sum of numbers from 1 to 5 is 15
"""
