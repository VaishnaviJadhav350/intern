#....String....

s = "PythonProgramming"
print(s[0])   # first character
print(s[4])   # 5th character
print(s[-10])   # 10th character from end
print(s[-5])    # 5th character from end
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string

z = "Java"
for char in z:
    print(char)

a = "Java"
del a

s1 = "P" + s[1:]   # update first character
s2 = s.replace("Python", "PythonProgramming")  # replace word
print(s1)
print(s2)

s = "PythonProgramming"
print(len(s))

s = "Hello World"
print(s.upper())
print(s.lower())

s = "   Java   "
print(s.strip()) # strip: removed the white spaces   

s = "Python is fun"
print(s.replace("fun", "simple"))

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello "
print(s * 3)



#....List.....

a = [10, 20, 30, 40, 50]
print("Original List:", a)

# 1. append() - add an element at the end
a.append(60)
print("After append(60):", a)

# 2. insert() - insert element at a specific index
a.insert(2, 25)
print("After insert(2, 25):", a)

# 3. extend() - add multiple elements
a.extend([70, 80])
print("After extend([70, 80]):", a)

# 4. remove() - remove first occurrence of a value
a.remove(25)
print("After remove(25):", a)

# 5. pop() - remove element at a given index (default last)
popped_item =a.pop(3)
print("After pop(3):", a, "| Popped item:", popped_item)

# 6. index() - find index of a value
index= a.index(20)
print("Index of 20:", index)

# 7. count() - count occurrences of a value
count_20 = a.count(20)
print("Count of 20:", count_20)

# 8. sort() - sort the list
a.sort()
print("After sort():", a)

# 9. reverse() - reverse the list
a.reverse()
print("After reverse():", a)

# 10. copy() - make a shallow copy
new_list = a.copy()
print("Copy of list:", new_list)

# 11. clear() - remove all elements
a.clear()
print("After clear():", a)



#....Tuple....

a = (1, 2, 3, 2, 4, 5)

# 1. count() - counts occurrences of a value
count= a.count(2)
print("Count of 2:", count)

# 2. index() - finds index of first occurrence of a value
index = a.index(4)
print("Index of 4:", index)

# Convert tuple to list for mutable operations
b = list(a)
print(b)

# 3. append() equivalent - adding element
b.append(6)
print("After append:", tuple(b))

# 4. insert() equivalent - inserting element at a specific index
b.insert(2, 10)
print("After insert at index 2:", tuple(b))

# 5. remove() equivalent - removing an element
b.remove(2)  # removes first occurrence of 2
print("After removing 2:", tuple(b))

# 6. pop() equivalent - remove element by index
b.pop(3)
print("After pop at index 3:", tuple(b))

# 7. slicing (works directly on tuple)
print("Slice from index 1 to 4:", a[1:5])

# 8. concatenation
b = (7, 8)
combined = a + b
print("Concatenated tuple:", combined)

# 9. repetition
repeated = a * 2
print("Repeated tuple:", repeated)



#....Dictionary....

a = {"name": "Vaishnavi", "age": 18, "city": "Pune"}

# 1. get()
print("Get name:", a.get("name"))

# 2. keys()
print("Keys:", a.keys())

# 3. values()
print("Values:", a.values())

# 4. items()
print("Items:", a.items())

# 5. setdefault()
a.setdefault("country", "India")
print("After setdefault:", a)

# 6. update()
a.update({"age": 19, "city": "Mumbai"})
print("After update:", a)

# 7. pop()
a.pop("age")
print("After pop age:", a)

# 8. popitem()
a.popitem()
print("After popitem:", a)

# 9. clear()
temp = a.copy()
temp.clear()
print("After clear:", temp)

# 10. copy()
copy_a = a.copy()
print("Copy of a:", copy_a)

# 11. fromkeys()
new_dict = dict.fromkeys(["x", "y", "z"], 0)
print("From keys:", new_dict)

# 12. del
del a["name"]
print("After del name:", a)

# 13. len()
print("Length of dictionary:", len(a))

# 14. in operator
print("Is 'city' in dictionary?", "city" in a)



#....Set....

a = {1, 2, 3, 4, 5}

print("Original set:", a)

# 1. add()
a.add(6)
print("After add(6):", a)

# 2. update()
a.update([7, 8])
print("After update([7, 8]):", a)

# 3. remove()
a.remove(3)
print("After remove(3):", a)

# 4. discard()
a.discard(10)   # no error if element not present
print("After discard(10):", a)

# 5. pop()
a.pop()
print("After pop():", a)

# 6. copy()
b = a.copy()
print("Copy of set:", b)

# 7. clear()
b.clear()
print("After clear():", b)


# Create another set for set operations
c = {4, 5, 9, 10}
a = {2, 4, 5, 6, 7, 8} 

# 8. union()
print("Union:", a.union(c))

# 9. intersection()
print("Intersection:", a.intersection(c))

# 10. difference()
print("Difference (a - c):", a.difference(c))

# 11. symmetric_difference()
print("Symmetric Difference:", a.symmetric_difference(c))

# 12. len()
print("Length of set a:", len(a))
print("Length of set a:", len(c))

# 13. in operator
print("Is 4 in set a?", 4 in a)


