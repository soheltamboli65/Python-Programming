# Creating a list
list1 = [1, 2, 3, 4, 5]

# Concatenation: Combining list1 with another list
list2 = [6, 7, 8]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

# Repetition: Repeating list1 two times
repeated_list = list1 * 2
print("Repeated List:", repeated_list)

# Membership: Checking if an element is in the list
element_to_check = 3
if element_to_check in list1:
    print(f"{element_to_check} is in list1.")
else:
    print(f"{element_to_check} is not in list1.")

# Manipulating list elements: 
# Changing the 2nd element (index 1) of list1
list1[1] = 10
print("List after modifying element at index 1:", list1)

# Adding a new element at the end of list1
list1.append(6)
print("List after appending a new element:", list1)

# Inserting an element at a specific position (index 2)
list1.insert(2, 15)
print("List after inserting 15 at index 2:", list1)

# Removing an element from the list
list1.remove(10)
print("List after removing element 10:", list1)
