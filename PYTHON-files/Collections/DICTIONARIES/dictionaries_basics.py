        # Dictionaries are: #
'''Mutable, Ordered (3.7), No Duplicates'''

# using curly braces with key:value pairs
this_dict = {"fruits": ["apple", "banana"], "flower": ["tulip", "rose"] }    # Commmonly Used this
print(this_dict)

# Using the dict() function
this_dict = dict(fruits = ["apple","banana"], flowers = ["tulip", "rose"])
print(this_dict)

# ACCESSING DICT
# Access items by using square braces
print("Fruits are:", this_dict["fruits"])

# Access by get() method
print("Fruits are:", this_dict.get("fruits"))

# Access by dict values() method
all_keys = this_dict.keys()
all_values = this_dict.values()
print(all_keys)
print(all_values)

# items() function for access as tuple for key:value pairs
items = this_dict.items()
print(items)
###

# Dictionary length
print(len(this_dict))       # Counts only individual key:value pairs i.e 2 here

# Finding type
print(type(this_dict))

# str 
print(str(this_dict))

# Membership operator 
if "fruits" in this_dict:   # Searches key in the dictionary
    print("Apple in this list")

