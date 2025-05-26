            # Sets are: #
'''Mutable, Unordered, Dont allow Duplicates'''

# Using curly braces
my_set = {1, 2, 3, 4}     # Commmonly Used this
print(my_set)

# Using the set() function
another_set = set([1, 2, 2, 3, 4])
print(another_set)  # Duplicates are removed

my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}

my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}
my_set.discard(10) 

# Create a frozenset from a list
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)  # frozenset({1, 2, 3, 4})

# Create a frozenset from a set
another_frozenset = frozenset({4, 5, 6})
print(another_frozenset)  # frozenset({4, 5, 6})