"""
--------------------------------------------------
--- Recursion Function ---
--------------------------------------------------
 A Function is said to be recursive if it calls itself
"""

"""
Factorial of a number
5*4*3*2*1
4*3*2*1

n*(n-1)....1

7!



--------------------------------------------------
What is the factorial of a number?
A factorial is represented by a number and a  ” ! ”  mark at the end. 
Factorial of a non-negative integer is the multiplication of all positive integers smaller than or equal to n
It is widely used in permutations and combinations to calculate the total possible outcomes. 

For example factorial of 6 is 6*5*4*3*2*1 which is 720

n(n-1)(n-2)....1

"""

def factorial(n):
    fact=1
    if n<0:
        print("Factorial Can not be negative")
    else:
        for i in range(1,n+1):
            fact=fact*i
            print(fact)


"""
itration          factorial (returned Value)
i=1    factorial 1               1*1=1
i=2    2 factorial 1               1*2=2
i=3    3 factorial 2              2*3=6
i=4    4 factorial 3           6*4=24
i=5    5 factorial 4            24*5=120
i=6    6 factorial 5              120*6=720  
i=7    7 factorial 6             720*7=5040 



"""

def Madrwwb(num):
    return num* Madrwwb(num-1)





def factorial(n):
    if n == 1:
        return 1     # base case
    else:
        return (n * factorial(n-1)) #

num = 7
result = factorial(num)
print(result)

"""
----------------------
--- Assignment ---
----------------------
Remove duplicate character from given string using Recursion Like [ WWWoooorrrlllddd] return World
"""
