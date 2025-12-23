## Function
"""A function is a named block of code that is written once and can be used many times to perform a specific task.
    Types:  1. Built in function
            2. User defined function"""
   
#....1] Built in Function
"""A built-in function is a function that is already provided by Python."""

print("Hello")
length = len("Python")
num = int("10")

import math;
m=max(20,35)
print("Largest Number=",m)
m=min(20,35)
print("Smallest Number=",m)
m=pow(2,3)
print("Power of 2^3 =",m)
m=round(20.55)
print("Rounded Number=",m)
m=abs(-23)
print("Abs Result=",m)
m=math.ceil(8.1)
print("Ceil Number=",m)
m=math.floor(8.1)
print("Floor Number=",m)


#....2] User defined Function
"""A user-defined function is a function created by the programmer to perform a specific task."""

#function without parameters
def greeting():
    print("Welcome to the python!!")
greeting()


# Function with parameters
# Add 2 numbers:
def add2num(a, b):
    result= a+b
    print("The sum is:", result)
add2num(5, 3)

# Function with return Statements
def add2num(a, b):
    return a+b
result = add2num(2,23)
print (result)


# Function with arguments
""" Type: 1] Required arguments
          2] Default arguments
          3] Keyword argument
          4] Arbitary arguments """

# 1] Required argument
def arg(name):
    print("Hello",name)
arg("Vaishu")

# 2] Default argument
def arg(name="Python"):
    print("Hello",name)
arg()
arg("World")

# 3] Keyword arguments
def arg(a, b):
    return a/b
result1 =arg(10,5)
print(result1)

result2 = arg(b=10, a=5)
print(result2) 

# 4] Arbitary arguments
# *args :-Numbers without names/access any number of positional argument

def add(*nums):
    print(nums)

add(10, 20, 30)


def greeting(*names):
    for name in names:
        print(f"Hello, {name}!")
greeting("Madhav","Vaishnavi","Rishabh")

# **kwargs :- Values with names/ key-value pair

def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Amit", age=20, city="Pune")

# *args, **kwargs :-

def info(*args, **kwargs):
    print(args)
    print(kwargs)

info(10, 20, name="Riya", age=21)


#....Lambda Function...
"""A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression."""

x = lambda a : a + 10
print(x(5))

x= lambda a, b : a * b
print(x(5, 7)) #....Multiply argument a with argument b and return the result


# Use that function definition to make a function that always doubles the number 
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

#... Lambda with Built-in Functions...
"""Lambda functions are commonly used with built-in functions like map(), filter(), and sorted()."""

#...The map() function
"""applies a function to every item in an iterable /  List मधील प्रत्येक value वर operation करायचा असेल"""

nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))
print(result)

#....The filter() function 
"""creates a list of items for which a function returns True/  Condition based values काढायच्या असतील"""

nums1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 != 0, nums1))
print(result)

#....reduce() function
"""Multiple values combine करायच्या असतील"""

from functools import reduce
num = [1, 2, 3, 4]
result = reduce(lambda a, b : a+b,num)
print(result)

#....Sort() function
"""The sorted() function can use a lambda as a key for custom sorting"""

students = [(1, 50), (2, 80), (3, 60)]
students.sort(key=lambda x: x[1])
print(students)


#.....Recursive Function.....
"""Function calling itself = Recursion"""

def print_num(n):
    if n == 0:        # base case
        return
    print(n)
    print_num(n-1)    # recursive call
print_num(5)

#... Factorial
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)
print(factorial(5))


#.....Scope.....
""" A variable is only available from inside the region it is created. This is called scope."""

# ...Local Scope
"""A variable created inside a function belongs to the local scope of that function, and can only be used inside that function."""

def func():
  x = 300
  print(x)
func()

# ...Global scope
"""Global variables are available from within any scope, global and local"""

x=56
def func():
    print(x)
func()
print(x)

"""If you need to create a global variable, but are stuck in the local scope, you can use the global keyword."""

def func():
    global x
    x=45
    print(x)
func()
