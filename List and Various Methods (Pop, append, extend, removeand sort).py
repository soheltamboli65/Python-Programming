# Creating an initial list
List = [3, 4, 5, 1,2, 5, 9,8]

# append(): 
List.append(6)
print("List after append(6):", List)

# extend(): 
List.extend([7, 10])
print("List after extend([7, 8]):", List)

# pop(): 
popped_element = List.pop()         # By default removes the last element

print("Popped element:", popped_element)
print("List after pop():", List)

# remove():

List.remove(1)  
print("List after remove(1):", List)

# sort(): 
List.sort()
print("List after sort():", List)
