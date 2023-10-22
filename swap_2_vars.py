# Version: 2.0
# Author: Bevlin Reddy

# Objective: swap two variables withouth a 3 variable
# if I start with x = 1 and y = 4, then without a third variable x = 4 and y = 1

# ToDo: Is this the only strategy to solve this? and
# ToDo: Are these the fewest lines?

x = 321
y = 1024

# two strategies to solve the problem
process = int(input("Addition and Subtraction: (1) or Multiplication and Division: (2)__"))

if process == 1:
    x = x + y
    y = x - y       # y is now = x
    x = x - y       # x is now = y
    print("Solved with additional.")
    print("x = ",x)
    print("y = ",y)
elif process == 2:
    x = x * y
    y = x / y       # y is now = x
    x = x / y       # x is now = y
    print("Solved with multiplication.")
    print("x = ",x)
    print("y = ",y)

else:
    print("Error in solution strategy.")

# FixMe:
