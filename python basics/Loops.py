
## LOOPS ##


#....For Loop....
"""The for loop is used when we know how many times the loop should run."""

# Print 1 to 5 numbers
for i in range(1, 6):
    print(i)

# Print odd or even numbers
for i in range(1, 20, 2):
    print(i)
for i in range(2, 20, 2):
    print(i)


#....While....
"""The while loop runs as long as a condition is true."""

# print 1 to 5 numbers
i = 1
while i <= 5:
    print(i)
    i = i + 1


# Factorial
n = int(input("Enter number: "))
fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)


#....break....
"""Stops the loop completely."""

for i in range(5):
    if i == 3:
        break
    print(i)

#....Continue....
"""Skips the current iteration."""

for i in range(5):
    if i == 2:
        continue
    print(i)


#....Pass....
"""Does nothing (used as a placeholder)."""

for i in range(3):
    pass