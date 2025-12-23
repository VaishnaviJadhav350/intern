#.. Module..
"""A module is a Python file (.py) that contains functions, variables, or classes.
It helps us organize code and reuse it in other programs.
    Types: 1] Built in module
           2] User defined module"""

# 1] Built-in Modules
"""Modules already available in Python."""

"""Examples:
math
random
datetime """

import math
print(math.sqrt(16))

import math
import cmath

#math module functions
x=math.ceil(1.1)
print("Result of ceil(1.1) =",x)
x=math.floor(1.1)
print("Result of floor(1.1) =",x)
x=math.trunc(1.1)
print("Result of trunc(1.1) =",x)
x=math.factorial(5)
print("Result of factorial(5) =",x)
x=math.sin(90)
print("Result of sin(90) =",x)
x=math.cos(60)
print("Result of cos(60) =",x)
x=math.pow(2,3)
print("Result of pow(2,3) =",x)
x=math.sqrt(9)
print("Result of sqrt(9) =",x)

#cmath module functions
m=2+2j
print("Result of exp(2+2j) =",cmath.exp(m))
x=cmath.log(m,2)
print("Result of log(2+2j,2) =",x)
x=cmath.sqrt(m)
print("Result of sqrt(2+2j) =",x)

# Random module
import random
print(random.choice([10, 20, 30]))

# sys module (system information)
import sys
print(sys.version)

# time module
import time
print(time.time())

# Calender
import calendar
print(calendar.month(2025, 1))

# Datetime
import datetime
print(datetime.date.today())



# 2] User-Defined Modules
"""Modules created by the programmer."""

import calci

print(calci.add(10, 5))
print(calci.sub(10, 5))
print(calci.mul(10, 5))
print(calci.div(10, 5))
print(calci.sqr(7))

from calci import add, sub, mul, div, sqr
print(add(3, 4))
print(sub(4, 4))
print(div(12, 4))
print(mul(3, 4))
print(sqr(5))