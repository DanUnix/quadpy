# Quadratic Equation Solver
# Author: Daniel Pulley
# Date: March 9th, 2016
# Description: Program Prompts user for a,b,c values and gives tthe results of the quadratic equation
# Practicing Python Basics

# import math for square root function
import math

# Discriminant = (b^2-4(a)(c))
def discriminant(a,b,c):
    # b^2 
    b = math.pow(b, 2) 
    # (b^2-4(a)(c))
    radicand = (b -((4)*(a)*(c)))

    # If Radicand is negative then exit program
    # Can't take square root of negative values
    if radicand < 0:
        print'Your radicand ', radicand, 'is negative and cannot be squared!'
        quit()
    # Take the square root of our randicand to get discriminant
    dis = math.sqrt(radicand)
    # return discriminant
    return dis

# Prompt User for variables
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# get discriminant value from function
mydis = discriminant(a,b,c)

# Quadratic Equation has to Answers
X1 = (((-b) + mydis)/(2*a))    
X2 = (((-b) - mydis)/(2*a))

# Print results to users
print("Answer 1 = ",X1)
print("Answer 2 = ",X2)
    
    
