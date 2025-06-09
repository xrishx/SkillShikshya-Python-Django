            # Tuples are: #
'''Immutable, Ordered, Allow Duplicates'''

# using small braces
my_tuple = (1, 2, 3, 4)     # Commmonly Used this
print(my_tuple)

# Using the list() function
another_tuple = tuple((1, 2, 2, 3, 4))
print(another_tuple)  # Duplicates are not removed


# Lists length
print(len(my_tuple))

# Access Tuple items by indexing
this_tuple = ("apple", "banana", "cherry")
print(this_tuple[1])     # indexing starts at 0

# Negative indexing also works
print(this_tuple[-1])

# Range of index works too
print(this_tuple[1:3])

# Membership operator 
if "apple" in this_tuple:
    print("Apple in this list")
