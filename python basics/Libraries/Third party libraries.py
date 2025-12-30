import numpy
import pandas

print("NumPy and Pandas are installed")


##....Numpy....
"""NumPy (Numerical Python) is a library used for numerical calculations and working with arrays."""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
# operations
print(arr.dtype)
arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype)
print("Array:", arr)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Multiply by 2:", arr * 2)
print(arr[1])         # .......... Get the second Element
print(arr[2] + arr[3])          #...........Get the Addition of third and fourth element
print(arr[1:5])        #............Slice elements from index 1 to index 5 from the following array
print(arr[4:])        #............Slice elements from index 4 to the end of the array
print(arr[:4])         #...........Slice elements from the beginning to index 4 (not included)

for x in arr:
  print(x)   #.........Iterate on the elements of the following 1-D array

newarr = arr.astype('f')          #..........Change data type from integer to float by using 'f' as parameter value
print(newarr.dtype)
x = arr.copy()         #..........Copy the array
print(x)

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr3.reshape(4, 3)          #..........The outermost dimension will have 4 arrays, each with 3 elements
print(newarr1)

newarr2 = arr3.reshape(2, 2, 3)
print(newarr2)       #..........The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements

arr4 = np.array([[1, 2, 3], [4, 5, 6]])     #........Iterate on the elements of the following 2-D array
for y in arr4:
  print(y)




##....Pandas...
"""Pandas is a library used for data analysis and data handling (tables like Excel)."""

import pandas as pd

# create DataFrame : Two-dimensional data, Like an Excel table . Has rows and columns
data = {
    "Name": ["Amit", "Neha", "Ravi"],
    "Age": [20, 21, 19]
}
df = pd.DataFrame(data)
print(df)


# Series : 
"""One-dimensional data , Like a single column . Can store numbers, strings, etc."""

s = pd.Series([10, 20, 30])
print(s)

