# Tuple is immutable or unchangebale
# BUT can convert it to list, change it then convert it back

this_tuple = ("apple", "pineapple", "mango")

# ADD ITEMS
# To ADD items using list
to_list = list(this_tuple)
to_list.append("orange")
this_tuple = tuple(to_list)
print(this_tuple)

# To ADD tuple to tuple
another_tuple = ("water", "coke", "fanta")
this_tuple += another_tuple
print(this_tuple)

# REMOVE ITEMS
# To REMOVE items using list
to_list = list(this_tuple)
to_list.remove("apple")
this_tuple = tuple(to_list)
print(this_tuple)

# Using del to delete the tuple completely
del this_tuple
print(this_tuple) # will give error as tupple no longer exists

