# Original tuple
tuple = (1, 2, 3, 4, 5)

# Access elements by index
print(tuple[2])  # Output: 3

# Slicing the tuple
print(tuple[1:4])  # Output: (2, 3, 4)

# Concatenating tuples
tuple2 = (6, 7)
tuple3 = tuple + tuple2  # Concatenate tuple and tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Repeating a tuple
tuple_repeated = tuple * 2  # Repeat tuple twice
print(tuple_repeated)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Length of the tuple
print(len(tuple))  # Output: 5
