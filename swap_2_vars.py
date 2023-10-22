# Version: 1.0
# Author: Bevlin Reddy

# Objective: swap two variables withouth a 3 variable
# if I start with x = 1 and y = 4, then without a third variable x = 4 and y = 1

x = 321
y = 1024

x = x + y
y = x - y       # y is now = x
x = x - y       # x is now = y

print("x = ",x)
print("y = ",y)

# TODO: Is this the fewest number of lines?
# FixMe:
