import copy

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
news_dict = new_dict.copy()
# also can do
news_dict = dict(new_dict)

# Shallow copy changes the original list as well
# Deep copy doesn't change the original list when edited
deepcopy_newdict = copy.deepcopy(new_dict) # have to import copy


        # Nested Dictionaires
# Dictionary inside a dictionary

# Direct Method
nested_dict = {
    "Fruits": {"Yummy": "apple", "Yucky": "guava"},
    "Flower": {"Like": "tulip", "loathe": "rose"}
}   
print(nested_dict)

# Using Loop
nested_dict = {}
parameters = ["Fruits", "Colors"]
for key in parameters:
    nested_dict[key] = {"Yummy": "Orange", "Lovely": "blueberry"}
print(nested_dict)


## Adding to Nested Dict
# Adding a new key-value pair to Fruits's nested dictionary
nested_dict["Fruits"]["Like"] = "Blackberry"
print(nested_dict)
# Adding new nested dict
nested_dict["Sports"] = {"Can play": "Football", "CAnt play": "Basketball"}
print(nested_dict)

## Accessing in Nested Dict
# Direct Indexing
yummy_fruits = nested_dict["Fruits"]["Yummy"]
print("Yummy fruit is:", yummy_fruits)
# Using get() method
loathe_flower = nested_dict.get("Flower", {}).get("loathe", "Not Found") 
# returns Not Found if doesnt exist instead of error
print("Loathe Flower:", loathe_flower)  

## Deleting in Nested Dict
# use del
del nested_dict["Sports"]
print(nested_dict)