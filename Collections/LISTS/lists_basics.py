            # Lists are: #
'''Mutable, Ordered, Allow Duplicates'''

# using large braces
this_list = [1, 2, 3, 4]    # Commmonly Used this
print(this_list)

# Using the list() function
another_list = list((1, 2, 2, 3, 4))
print(another_list)  # Duplicates are not removed

# Lists length
print(len(this_list))

# Access List items by indexing
this_list = ["apple", "banana", "cherry"]
print(this_list[1])     # indexing starts at 0

# Negative indexing also works
print(this_list[-1])

# Range of index works too
print(this_list[1:3])

# Membership operator 
if "apple" in this_list:
    print("Apple in this list")

