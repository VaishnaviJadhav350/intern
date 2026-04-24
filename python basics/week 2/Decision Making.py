## Decision Making ##

# ... if Statement ...
"""Executes a block of code only if the condition is True."""

# ckeck the number is positive or not
n=5
if n>=0:
    print("Number is positive")

# Ckeck Pass or Fail
a=int(input("Enter your Marks: "))
if a>=36:
    print("PASS")

# Check user login
username = "Admin"
password = "abc@123"
if username=="Admin" and password=="abc@123":
    print("Login successful")
 

#...if-else statement...
"""Executes one block if condition is True, otherwise executes the else block."""

#Check the number is positive or not
num=34
if num>=0:
    print("Number is positive")
else:
    print("Number is negative")


#Check user login
username=input("Enter your Username: ")
password=input("Enter ypur secret password:")
if username=="Learning" and password=="pass@123":
    print("Login Successful")
else:
    print("Invalid username and password")


#Check number is even or odd
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#...if-elif-else ladder...
"""Used to check multiple conditions. Only one condition can executed"""

marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")



## Student Result Menu

print("---- MENU ----")
print("1. Check Pass or Fail")
print("2. Check Grade")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    marks = int(input("Enter marks: "))
    if marks >= 35:
        print("PASS")
    else:
        print("FAIL")

elif choice == 2:
    marks = int(input("Enter marks: "))
    if marks >= 75:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 35:
        print("Grade: C")
    else:
        print("Grade: F")

elif choice == 3:
    print("Exit Program")

else:
    print("Invalid choice")
