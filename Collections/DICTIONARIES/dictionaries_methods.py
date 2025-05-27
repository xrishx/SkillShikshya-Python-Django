this_dict = {"name":"Rishav", "age":24 , "year":2000}

# Update the item by referring it's key name
this_dict['year'] = 2025
print(this_dict)

    # update() method
# To update existing item
this_dict.update({"year":2000})
print(this_dict)

# To add new item
this_dict.update({"mood":"hungry"})
print(this_dict)

    # pop() method
# Remove item with specified name
this_dict.pop("mood")
print(this_dict)

    # popitem() method
# Removes the last inserted item
this_dict.popitem()
print(this_dict)

# del this_dict["mood"]       # does the same as pop()
# del this_dict               # deletes the entire dict

    # clear() method
# Clears the dict    
this_dict.clear()

    # dict.fromkeys() methpd
# Create a new dict with keys from seq and values set to value
name = "Rishav"
value = "1"
new_dict = dict.fromkeys(name, value)
print(new_dict)

    # copy() method
# copy the dict
new_dict = new_dict.copy()
# also can do
new_dict = dict(new_dict)

# Shallow copy changes the original list as well
# Deep copy doesn't change the original list when edited
